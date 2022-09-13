import binascii
import logging
import re
from typing import (
    Any,
    Dict,
    List,
    Tuple,
    Union,
    cast,
)

from PyPDF2._cmap import (
    _default_fonts_space_width,
    compute_space_width,
    parse_bfchar,
    parse_encoding,
    prepare_cm,
    unknown_char_map,
)
from PyPDF2.errors import PdfStreamError
from PyPDF2.generic import (
    ContentStream,
    DictionaryObject,
    NameObject,
)

from .text_collector import TextCollector

elsevier_regexp = re.compile(
    r'Downloaded for .* at .* from .* '
    r'by .* on \w+ \d{1,2}, \d{4}. '
    r'For personal use only. No other uses without permission. '
    r'Copyright ©\d{4}. Elsevier Inc. All rights reserved.'
)
bmj_regexp = re.compile(
    r'^.*: first published as .* on \d{1,2} \w+ \d{4}. Downloaded from .*'
    r' on \w+ \d{1,2}, \d{4} at .* Protected by\s*copyright.'
)
downloaded_regexp = re.compile(rb'^[Dd]ownloaded [Ff]rom:? https?://')
terms_of_use_regexp = re.compile(rb'^[Tt]erms [Oo]f [Uu]se:? https?://')


def _is_downloaded_from_https_watermark(text):
    return bool(re.search(downloaded_regexp, text)) or bool(re.search(terms_of_use_regexp, text))


def _is_1021_watermark(text):
    return (
        text.startswith(b'Downloaded via ')
        or text.startswith(
            b'See https://pubs.acs.org/sharingguidelines for options '
            b'on how to legitimately share published articles.'
        )
    )


def _is_1093_watermark(text):
    return bool(re.search(rb'^Downloaded from https://(.*) by [\w\s]+ on \d{1,2} \w+ \d{4}$', text))


def process_cm_line(
    l: bytes,
    process_rg: bool,
    process_char: bool,
    multiline_rg: Union[None, Tuple[int, int]],
    map_dict,
    int_entry,
):
    if l in (b"", b" ") or l[0] == 37:  # 37 = %
        return process_rg, process_char, multiline_rg
    if b"beginbfrange" in l:
        process_rg = True
    elif b"endbfrange" in l:
        process_rg = False
    elif b"beginbfchar" in l:
        process_char = True
    elif b"endbfchar" in l:
        process_char = False
    elif process_rg:
        multiline_rg = parse_bfrange(l, map_dict, int_entry, multiline_rg)
    elif process_char:
        parse_bfchar(l, map_dict, int_entry)
    return process_rg, process_char, multiline_rg


def parse_bfrange(
    l: bytes,
    map_dict: Dict[Any, Any],
    int_entry: List[int],
    multiline_rg: Union[None, Tuple[int, int]],
) -> Union[None, Tuple[int, int]]:
    lst = [x for x in l.split(b" ") if x]
    closure_found = False
    nbi = len(lst[0])
    map_dict[-1] = nbi // 2
    fmt = b"%%0%dX" % nbi
    if multiline_rg is not None:
        a = multiline_rg[0]  # a, b not in the current line
        b = multiline_rg[1]
        for sq in lst[1:]:
            if sq == b"]":
                closure_found = True
                break
            map_dict[
                binascii.unhexlify(fmt % a).decode(
                    "charmap" if map_dict[-1] == 1 else "utf-16-be",
                    "surrogatepass",
                )
            ] = binascii.unhexlify(sq).decode("utf-16-be", "surrogatepass")
            int_entry.append(a)
            a += 1
    else:
        a = int(lst[0], 16)
        b = int(lst[1], 16)
        if lst[2] == b"[":
            for sq in lst[3:]:
                if sq == b"]":
                    closure_found = True
                    break
                map_dict[
                    binascii.unhexlify(fmt % a).decode(
                        "charmap" if map_dict[-1] == 1 else "utf-16-be",
                        "surrogatepass",
                    )
                ] = binascii.unhexlify(sq).decode("utf-16-be", "surrogatepass")
                int_entry.append(a)
                a += 1
        else:  # case without list
            c = int(lst[2], 16)
            fmt2 = b"%%0%dX" % max(4, len(lst[2]))
            closure_found = True
            while a <= b:
                map_dict[
                    binascii.unhexlify(fmt % a).decode(
                        "charmap" if map_dict[-1] == 1 else "utf-16-be",
                        "surrogatepass",
                    )
                ] = binascii.unhexlify(fmt2 % c).decode("utf-16-be", "surrogatepass")
                int_entry.append(a)
                a += 1
                c += 1
    return None if closure_found else (a, b)


def parse_to_unicode(ft: DictionaryObject, space_code: int):
    # will store all translation code
    # and map_dict[-1] we will have the number of bytes to convert
    map_dict = {}

    # will provide the list of cmap keys as int to correct encoding
    int_entry = []

    if "/ToUnicode" not in ft:
        return {}, space_code, []
    process_rg: bool = False
    process_char: bool = False
    multiline_rg: Union[
        None, Tuple[int, int]
    ] = None
    cm = prepare_cm(ft)
    for l in cm.split(b"\n"):
        process_rg, process_char, multiline_rg = process_cm_line(
            l.strip(b" "), process_rg, process_char, multiline_rg, map_dict, int_entry
        )

    for a, value in map_dict.items():
        if value == " ":
            space_code = a
    return map_dict, space_code, int_entry


def build_char_map(
    font_name: str, space_width: float, obj: DictionaryObject
):  # font_type,space_width /2, encoding, cmap
    ft: DictionaryObject = obj["/Resources"]["/Font"][font_name]  # type: ignore
    font_type: str = cast(str, ft["/Subtype"])

    space_code = 32
    encoding, space_code = parse_encoding(ft, space_code)
    map_dict, space_code, int_entry = parse_to_unicode(ft, space_code)

    if encoding == "":
        if -1 not in map_dict or map_dict[-1] == 1:
            encoding = "charmap"
        else:
            encoding = "utf-16-be"
    elif isinstance(encoding, dict):
        for x in int_entry:
            if x <= 255:
                encoding[x] = chr(x)
    try:
        # override space_width with new params
        space_width = _default_fonts_space_width[cast(str, ft["/BaseFont"])]
    except Exception:
        pass
    # I conside the space_code is available on one byte
    if isinstance(space_code, str):
        try:  # one byte
            sp = space_code.encode("charmap")[0]
        except Exception:
            sp = space_code.encode("utf-16-be")
            sp = sp[0] + 256 * sp[1]
    else:
        sp = space_code
    sp_width = compute_space_width(ft, sp, space_width)

    return (
        font_type,
        float(sp_width / 2),
        encoding,
        # https://github.com/python/mypy/issues/4374
        map_dict,
    )


class BasePdfProcessor:
    def __init__(self, remove_pages=None):
        self.remove_pages = remove_pages or tuple()

    def process_page(self, page, pdf_reader):
        return page

    def process(self, pdf_reader, pdf_writer):
        for page_num, page in enumerate(pdf_reader.pages):
            if page_num in self.remove_pages:
                continue
            try:
                page = self.process_page(page, pdf_reader)
            except (PdfStreamError, binascii.Error) as e:
                logging.getLogger('nexus_pylon').warning({
                    'action': 'pdf_stream_error',
                    'mode': 'pylon',
                    'error': str(e),
                })
            pdf_writer.add_page(page)


class BaseWatermarkEraser(BasePdfProcessor):
    def __init__(self, is_watermark_predicate=_is_downloaded_from_https_watermark, watermark_orientations=None, remove_pages=None):
        super().__init__(remove_pages=remove_pages)
        self.is_watermark_predicate = is_watermark_predicate
        self.watermark_orientations = watermark_orientations if watermark_orientations is not None else (0, 90, 180, 270)


class WatermarkEraser1(BaseWatermarkEraser):
    def process_page(self, page, pdf_reader):
        if '/XObject' in page['/Resources']:
            xobj = page['/Resources']['/XObject']
            content = ContentStream(page['/Contents'], pdf_reader, "bytes")

            xobj_death_note = []
            operations_death_note = []
            for op_i, (operands, operation) in enumerate(content.operations):
                if operation == b"Do":
                    nested_op = xobj[operands[0]]
                    if nested_op["/Subtype"] != "/Image":
                        text = page.extract_xform_text(nested_op, self.watermark_orientations, 200.0)  # type: ignore
                        if self.is_watermark_predicate(text.encode()):
                            xobj_death_note.append(operands[0])
                            operations_death_note.append(op_i)
                            logging.getLogger('nexus_pylon').debug({
                                'action': 'watermark_removal',
                                'mode': 'pylon',
                                'text': text,
                            })

            # Erase dictionary objects with watermarks
            for op_i in sorted(xobj_death_note, reverse=True):
                del xobj[op_i]

            # Erase operations with watermarks
            for op_i in reversed(operations_death_note):
                del content.operations[op_i]

            if operations_death_note or xobj_death_note:
                page.__setitem__(NameObject('/Contents'), content)
                page.compress_content_streams()

        return page


class WatermarkEraser2(BaseWatermarkEraser):
    def process_page(self, page, pdf_reader):
        content = ContentStream(page['/Contents'], pdf_reader, "bytes")
        operations_death_note = []

        for op_i, (operands, operation) in enumerate(content.operations):
            if operation == b"Tj":
                if isinstance(operands[0], bytes) and self.is_watermark_predicate(operands[0]):
                    operations_death_note.append(op_i)
                    logging.getLogger('nexus_pylon').debug({
                        'action': 'watermark_removal',
                        'mode': 'pylon',
                        'text': operands[0].decode(),
                    })

        # Erase operations with watermarks
        for op_i in reversed(operations_death_note):
            del content.operations[op_i]

        if operations_death_note:
            page.__setitem__(NameObject('/Contents'), content)
            page.compress_content_streams()

        return page


class WatermarkEraser3(BaseWatermarkEraser):
    def process_page(self, page, pdf_reader):
        content = ContentStream(page['/Contents'], pdf_reader, "bytes")
        operations_death_note = []

        for op_i, (operands, operation) in enumerate(content.operations):
            if operation == b"TJ":
                text = b''
                for operand in operands[0]:
                    if isinstance(operand, bytes):
                        text += operand
                if self.is_watermark_predicate(text):
                    operations_death_note.append(op_i)
                    logging.getLogger('nexus_pylon').debug({
                        'action': 'watermark_removal',
                        'mode': 'pylon',
                        'text': text.decode(),
                    })

        # Erase operations with watermarks
        for op_i in reversed(operations_death_note):
            del content.operations[op_i]

        if operations_death_note:
            page.__setitem__(NameObject('/Contents'), content)
            page.compress_content_streams()

        return page


class WatermarkEraser4(BaseWatermarkEraser):
    def __init__(self, regexp, inverted=False):
        super().__init__()
        self.regexp = regexp
        self.inverted = inverted

    def process_page(self, page, pdf_reader):
        content = ContentStream(page['/Contents'], pdf_reader, "bytes")
        operations_death_note = []

        cmaps = {}
        space_width = 200.0
        resources_dict = cast(DictionaryObject, page['/Resources'])
        tc = TextCollector(self.inverted)

        if "/Font" in resources_dict:
            for f in cast(DictionaryObject, resources_dict["/Font"]):
                cmaps[f] = build_char_map(f, space_width, page)

        cm_stack = []
        cmap = ("charmap", {}, "NotInitialized")

        for op_i, (operands, operation) in enumerate(content.operations):
            if operation == b"q":
                cm_stack.append(cmap)
            elif operation == b"Q":
                try:
                    cmap = cm_stack.pop()
                except Exception:
                    pass
            elif operation == b"Tf":
                try:
                    _space_width = cmaps[operands[0]][1]
                    cmap = (
                        cmaps[operands[0]][2],
                        cmaps[operands[0]][3],
                        operands[0],
                    )
                except KeyError:  # font not found
                    _space_width = unknown_char_map[1]
                    cmap = (
                        unknown_char_map[2],
                        unknown_char_map[3],
                        "???" + operands[0],
                    )
            elif operation == b"Tj":
                if isinstance(operands[0], str):
                    text = operands[0]
                else:
                    if isinstance(cmap[0], str):
                        try:
                            t = operands[0].decode(cmap[0], "surrogatepass")
                        except Exception:
                            t = operands[0].decode("utf-16-be" if cmap[0] == "charmap" else "charmap", "surrogatepass")
                    else:
                        t = "".join(
                            [
                                cmap[0][x] if x in cmap[0] else bytes((x,)).decode()
                                for x in operands[0]
                            ]
                        )
                    text = "".join([cmap[1][x] if x in cmap[1] else x for x in t])
                tc.add_piece(text, op_i)
                text, matched = tc.match(self.regexp)
                if matched:
                    operations_death_note.extend(matched)
                    logging.getLogger('nexus_pylon').debug({
                        'action': 'watermark_removal',
                        'mode': 'pylon',
                        'matched': text,
                    })
                    tc.clear()

        # Erase operations with watermarks
        for op_i in reversed(operations_death_note):
            del content.operations[op_i]

        if operations_death_note:
            page.__setitem__(NameObject('/Contents'), content)
            page.compress_content_streams()

        return page


pdf_processors = {
    '10.1001': WatermarkEraser1(watermark_orientations=(0,)),
    '10.1016': WatermarkEraser4(elsevier_regexp),
    '10.1021': WatermarkEraser1(is_watermark_predicate=_is_1021_watermark, watermark_orientations=(90,)),
    '10.1073': WatermarkEraser1(watermark_orientations=(90,)),
    '10.1088': WatermarkEraser1(is_watermark_predicate=lambda text: False, remove_pages=(0,)),
    '10.1093': WatermarkEraser2(is_watermark_predicate=_is_1093_watermark),
    '10.1126': WatermarkEraser1(watermark_orientations=(270,)),
    '10.1136': WatermarkEraser4(bmj_regexp, inverted=True),
    '10.1287': WatermarkEraser1(
        watermark_orientations=(90,),
        remove_pages=(0,),
    ),
    '10.2108': WatermarkEraser3(),
}

base_pdf_processor = BasePdfProcessor()
