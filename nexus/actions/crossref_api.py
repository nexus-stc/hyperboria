import time
from datetime import date

from nexus.models.proto.scimag_pb2 import Scimag as ScimagPb

from .base import BaseAction
from .exceptions import InterruptProcessing


def extract_authors(authors):
    result = []
    if authors:
        for author in authors:
            if 'family' in author and 'given' in author:
                result.append(f'{author["family"]}, {author["given"]}')
    return result


def extract_dates(date_parts):
    if not date_parts or not date_parts[0]:
        return 0, None
    year, month, day = date_parts[0] + [0] * (3 - len(date_parts[0]))
    if year:
        issued_at = int(time.mktime(date(
            year=year,
            month=month if month else 1,
            day=day if day else 1,
        ).timetuple()))
        return year, issued_at
    return 0, None


def extract_first(arr, default=''):
    if arr and len(arr) > 0:
        return arr[0]
    return default


def extract_page(page, default=0):
    np = ''
    for c in page:
        if c.isdigit():
            np += c
    if np:
        np = int(np)
        if np < 2**31:
            return np
    return default


def extract_pages(pages, default=0):
    try:
        if pages is None:
            return default, default
        pages = pages.split('-')
        if len(pages) == 2:
            return extract_page(pages[0], default=default), extract_page(pages[1], default=default)
        elif len(pages) == 1:
            return extract_page(pages[0], default=default), default
        return default, default
    except ValueError:
        return default, default


def extract_references(references):
    if references:
        dois = []
        for reference in references:
            if reference.get('DOI'):
                dois.append(reference['DOI'])
        return dois


def extract_title(title, subtitle):
    return ': '.join(filter(lambda x: bool(x), [title.strip(), subtitle.strip()]))


class ToThinScimagPbAction(BaseAction):
    async def do(self, item: dict) -> ScimagPb:
        if 'DOI' not in item:
            raise InterruptProcessing(document_id=None, reason='no_doi')
        return ScimagPb(doi=item['DOI'])


class ToScimagPbAction(BaseAction):
    async def do(self, item: dict) -> ScimagPb:
        if 'DOI' not in item:
            raise InterruptProcessing(document_id=None, reason='no_doi')
        scimag_pb = ScimagPb(
            abstract=item.get('abstract'),
            container_title=extract_first(item.get('container-title')),
            doi=item['DOI'],
            issue=item.get('issue'),
            issns=item.get('ISSN'),
            language=item.get('language'),
            ref_by_count=item.get('is-referenced-by-count'),
            references=extract_references(item.get('reference')),
            tags=item.get('subject'),
            title=extract_title(extract_first(item.get('title')), extract_first(item.get('subtitle'))),
            type=item.get('type'),
            volume=item.get('volume'),
        )
        if item.get('author'):
            scimag_pb.authors.extend(extract_authors(item['author']))
        elif item.get('editor'):
            scimag_pb.authors.extend(extract_authors(item['editor']))

        scimag_pb.first_page, scimag_pb.last_page = extract_pages(item.get('page'))
        scimag_pb.year, issued_at = extract_dates(item.get('issued', {}).get('date-parts'))
        if issued_at is not None:
            scimag_pb.issued_at = issued_at

        return scimag_pb
