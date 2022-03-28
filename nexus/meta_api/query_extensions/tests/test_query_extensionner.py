from nexus.meta_api.query_extensions import ClassicQueryProcessor
from nexus.meta_api.query_extensions.checks import QueryClass


def classic_query_processor(query):
    result = ClassicQueryProcessor().process(query, 'en')
    return result['query'], result['class']


def test_doi_query():
    assert classic_query_processor('10.1001/azeroth1021.azerty') == ('doi:"10.1001/azeroth1021.azerty"', QueryClass.DOI)
    assert classic_query_processor('https://doi.org/10.1001/azeroth1021.azerty') == (
        'doi:"10.1001/azeroth1021.azerty"', QueryClass.DOI
    )
    assert classic_query_processor('Gimme https://doi.org/10.1001/azeroth1021.azerty please') == (
        'doi:"10.1001/azeroth1021.azerty"', QueryClass.DOI
    )
    assert classic_query_processor('Gimme https://doi.org/10.1001/azeroth1021.azerty not 10.6666/kek please') == (
        'doi:"10.1001/azeroth1021.azerty"', QueryClass.DOI
    )
    assert classic_query_processor('10.1001 / test') == ('doi:"10.1001/test"', QueryClass.DOI)
    assert classic_query_processor('kek  10.1001  /  test') == ('kek OR 10.1001 OR test', QueryClass.Default)


def test_isbn_query():
    assert classic_query_processor('ISBN: 9784567890123') == ('isbns:9784567890123', QueryClass.ISBN)
    assert classic_query_processor('ISBN:9784567890123') == ('isbns:9784567890123', QueryClass.ISBN)
    assert classic_query_processor('ISBN: 978-4567890123') == ('isbns:9784567890123', QueryClass.ISBN)
    assert classic_query_processor('9784567890123') == ('isbns:9784567890123', QueryClass.ISBN)
    assert classic_query_processor('978-4567890123') == ('isbns:9784567890123', QueryClass.ISBN)


def test_url():
    assert classic_query_processor('https://www.google.com/lelkek') == (
        'https://www.google.com/lelkek',
        QueryClass.URL,
    )


def test_default():
    assert classic_query_processor('“Gay niggas in the space”') == (
        '"Gay niggas in the space"',
        QueryClass.Default,
    )
    assert classic_query_processor('“Gay niggas” in the space”') == (
        '"Gay niggas" OR in OR the OR space',
        QueryClass.Default,
    )
    assert classic_query_processor('Search “Gay niggas in the space”') == (
        'search OR "Gay niggas in the space"',
        QueryClass.Default,
    )
    assert classic_query_processor(
        'hemoglobin OR blood OR issued_at:978307200^0.65 OR '
        'issued_at:[1262304000 TO 1577836800]^0.65 '
        'wrong_field : 123 spaced_1: 123 spaced :2'
    ) == (
        'hemoglobin OR blood OR issued_at:978307200^0.65 OR '
        'issued_at:[1262304000 TO 1577836800]^0.65 '
        'OR wrong_field OR 123 OR spaced_1 OR 123 OR spaced OR 2',
        QueryClass.Default,
    )
    assert classic_query_processor('Gay Niggas: In the Space') == (
        'gay OR niggas OR in OR the OR space',
        QueryClass.Default,
    )
    assert classic_query_processor("Glass's Guide to Commercial Vehicles 1989") == (
        'glass OR s OR guide OR to OR commercial OR vehicles OR 1989',
        QueryClass.Default,
    )
