import re

from emoji import get_emoji_regexp

NON_ALNUMWHITESPACE_REGEX = re.compile(r'([^\s\w])+')
EMAIL_REGEX = re.compile(r'([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})')
EMOJI_REGEX = get_emoji_regexp()
HASHTAG_REGEX = re.compile(r'([#@]+)([A-Za-z0-9_]+)')
MULTIWHITESPACE_REGEX = re.compile(r"\s+")
STICKER_REGEX = re.compile(
    '^[\U0001F1E0-\U0001F1FF'
    '\U0001F300-\U0001F5FF'
    '\U0001F600-\U0001F64F'
    '\U0001F680-\U0001F6FF'
    '\U0001F700-\U0001F77F'
    '\U0001F780-\U0001F7FF'
    '\U0001F800-\U0001F8FF'
    '\U0001F900-\U0001F9FF'
    '\U0001FA00-\U0001FA6F'
    '\U0001FA70-\U0001FAFF'
    '\U00002702-\U000027B0]$',
    flags=re.UNICODE,
)
URL_REGEX = re.compile(r'^(https?|ftp)?:\/\/[^\s\/$.?#]+\.[^\s]*$')
HIDDEN_CHAR = '‌'
TELEGRAM_LINK_REGEX = re.compile('(?:https?://)?t\\.me/(?!joinchat/)([A-Za-z0-9_]+)')

DOI_REGEX = re.compile(r'(10.\d{4,9})\s?/\s?([-._;()<>/:A-Za-z0-9]+[^.?\s])')
ISBN_REGEX = re.compile(r'^(?:[iI][sS][bB][nN]\:?\s*)?((97(8|9))?\-?\d{9}(\d|X))$')
MD5_REGEX = re.compile(r'([A-Fa-f0-9]{32})')
NID_REGEX = re.compile(r'(?:[Nn][Ii][Dd]\s?:?\s*)([0-9]+)')
ONLY_DOI_REGEX = re.compile(r'^(10.\d{4,9})\s?/\s?([-._;()<>/:A-Za-z0-9]+[^.?\s])$')
PUBMED_ID_REGEX = re.compile(r'(?:(?:https?://)?(?:www.)?ncbi.nlm.nih.gov/pubmed/|[Pp][Mm][Ii][Dd]\s?:?\s*)([0-9]+)')
