from urllib.parse import unquote


def canonize_doi(doi):
    return unquote(doi.lower())
