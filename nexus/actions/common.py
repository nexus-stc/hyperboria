from urllib.parse import unquote


def canonize_doi(doi):
    return (
        unquote(doi.lower())
        .replace('\\n', '\n')
        .replace('\n', '')
        .replace('\\', '')
        .strip('\'"')
        .replace('\x00', '')
        .strip()
    )
