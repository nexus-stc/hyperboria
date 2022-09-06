import numpy as np
from izihawa_types.safecast import safe_int
from nexus.models.proto.scitech_pb2 import Scitech as ScitechPb

from .base import BaseAction

LANGUAGE_TRANSLATION = {
    'English': 'en',
    'Russian': 'ru',
    'German': 'de',
    'Ukrainian': 'uk',
    'French': 'fr',
    'Italian': 'it',
    'Spanish': 'es',
    'Portuguese': 'pt',
    'Chinese': 'zh',
    'Polish': 'pl',
    'english': 'en',
    'Russian-Ukrainian': 'ru,uk',
    'Russian-Ukrainian-English': 'en,ru,uk',
    'Russian(Old)': 'ru',
    'English-Russian': 'en,ru',
    'Turkish': 'tr',
    'Greek': 'el',
    'Romanian': 'ro',
    'Russian (Old)': 'ru',
    'Arabic': 'ar',
    'Français': 'fr',
    'Dutch': 'nl',
    'Japanese': 'ja',
    'Persian': 'fa',
    'Hungarian': 'hu',
    'Latin': 'la',
    'Serbian': 'sr',
    'Spanish;Castilian': 'es',
    'Spanish,Castilian': 'es',
    'German-Russian': 'de,ru',
    'Croatian': 'hr',
    'Lithuanian': 'lt',
    'Hebrew': 'iw',
    'French-Russian': 'fr,ru',
    'Czech': 'cs',
    'Kazakh': 'kz',
    'Swedish': 'sv',
    'Indonesian': 'id',
    'Greek(Modern)': 'el',
    'Chinese(PRC)': 'zh',
    'Belorussian': 'by',
    'Deutsch': 'de',
    'German-English': 'de,en',
    'English, German': 'de,en',
    'English-Ukrainian': 'en,uk',
    'English, French': 'en,fr',
    'Bulgarian': 'bg',
    'Romanian,Moldavian,Moldovan': 'mo',
    'Belarusian': 'by',
    'Finnish': 'fi',
    'Azerbaijani': 'az',
    'Bengali': 'bn',
    'English-French': 'en,fr',
    'English-German': 'de,en',
    'Chinese-English': 'en,zh',
    'chinese': 'zh',
    'Korean': 'ko',
}


def create_cu(libgen_id, coverurl, md5):
    cu_suf = ''

    bulk_id = (libgen_id - (libgen_id % 1000))
    proposed_coverurl = f"{bulk_id}/{md5}.jpg"
    proposed_coverurl_d = f"{bulk_id}/{md5}-d.jpg"
    proposed_coverurl_g = f"{bulk_id}/{md5}-g.jpg"

    if coverurl == proposed_coverurl:
        coverurl = ''
    elif coverurl == proposed_coverurl_d:
        cu_suf = 'd'
        coverurl = ''
    elif coverurl == proposed_coverurl_g:
        cu_suf = 'g'
        coverurl = ''
    return coverurl, cu_suf


class ToScitechPbAction(BaseAction):
    def process_tag(self, raw_tag) -> list:
        tags = []
        for tag in raw_tag.split(';'):
            tag = tag.strip().lower()
            if not bool(tag):
                continue
            for dash_tag in tag.split('--'):
                tags.append(dash_tag.strip())
        return list(sorted(set(tags)))

    def process_isbns(self, identifier):
        return list(filter(
            lambda x: bool(x),
            map(
                lambda x: x.replace('-', '').strip(),
                identifier.replace(';', ',').split(',')
            ),
        ))

    async def do(self, item: dict) -> ScitechPb:
        scitech_pb = ScitechPb(
            authors=(item.get('author') or '').split('; '),
            description=item.get('descr'),
            doi=item.get('doi'),
            edition=item.get('edition'),
            extension=item.get('extension'),
            filesize=safe_int(item['filesize']) or 0,
            is_deleted=item.get('visible', '') != '',
            isbns=self.process_isbns(item['identifier']),
            language=LANGUAGE_TRANSLATION.get(item['language']),
            libgen_id=int(item['id']),
            md5=item['md5'].lower(),
            pages=safe_int(item['pages']),
            series=item.get('series'),
            volume=item.get('volumeinfo'),
            periodical=item.get('periodical'),
            tags=self.process_tag(item['tags']),
            title=item['title'].replace('\0', '').strip(),
        )

        scitech_pb.cu, scitech_pb.cu_suf = create_cu(
            libgen_id=scitech_pb.libgen_id,
            coverurl=item['coverurl'].lower(),
            md5=scitech_pb.md5
        )
        year = safe_int(item['year'])
        if year and year < 9999:
            scitech_pb.year = year
            # Subtract 1970 because `np.datetime64(year, 'Y')` is not returning unixtime
            scitech_pb.issued_at = np.datetime64(year, 'Y').astype('datetime64[s]').astype(np.int64) - 62167132800
        return scitech_pb
