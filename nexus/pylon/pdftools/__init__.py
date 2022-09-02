import io

from PyPDF2 import (
    PdfReader,
    PdfWriter,
)
from PyPDF2.generic import DictionaryObject

from .watermarks import (
    base_pdf_processor,
    pdf_processors,
)


def is_pdf(f):
    return len(f) > 4 and f[:4] == b'%PDF'


def clean_metadata(pdf, doi=None):
    reader = PdfReader(io.BytesIO(pdf), strict=False)
    writer = PdfWriter()
    writer._objects = writer._objects[:-1]
    writer._info = writer._add_object(DictionaryObject())
    pdf_processor = base_pdf_processor
    if doi:
        doi_prefix = doi.split('/')[0]
        if doi_prefix in pdf_processors:
            pdf_processor = pdf_processors[doi_prefix]
    pdf_processor.process(reader, writer)
    buffer = io.BytesIO()
    writer.write_stream(buffer)
    buffer.flush()
    buffer.seek(0)
    return buffer.read()
