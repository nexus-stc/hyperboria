from urllib.parse import urlparse

fancy_names = {
}


def get_fancy_name(url):
    return fancy_names.get(urlparse(url).netloc.lower(), 'Saturn Rings')
