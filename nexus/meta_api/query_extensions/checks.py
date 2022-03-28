import re
from enum import Enum

from nexus.nlptools.regex import (
    DOI_REGEX,
    ISBN_REGEX,
    NID_REGEX,
    ONLY_DOI_REGEX,
    URL_REGEX,
)

# ToDo: redo all, code is logically incorrect now


class QueryClass(Enum):
    Default = 'default'
    DOI = 'doi'
    ISBN = 'isbn'
    NID = 'nid'
    URL = 'url'


def check_doi(query) -> (QueryClass, str):
    if (
        ((r := re.search(DOI_REGEX, query)) and re.search(URL_REGEX, query))
        or re.search(ONLY_DOI_REGEX, query)
    ):
        doi = (r[1] + '/' + r[2]).lower()
        return {
            'doi': doi,
            'query': f'doi:"{doi}"',
            'class': QueryClass.DOI,
        }


def check_isbn(query: str) -> (QueryClass, str):
    if r := re.search(ISBN_REGEX, query):
        isbn = r[1].replace('-', '')
        return {
            'isbn': isbn,
            'query': 'isbns:' + isbn,
            'class': QueryClass.ISBN
        }


def check_nid(query: str) -> (QueryClass, str):
    if r := re.search(NID_REGEX, query):
        return {
            'id': r[1],
            'query': 'id:' + r[1],
            'class': QueryClass.NID,
        }


def check_url(query: str) -> (QueryClass, str):
    if r := re.search(URL_REGEX, query):
        return {
            'url': r[0],
            'query': r[0],
            'class': QueryClass.URL,
        }
