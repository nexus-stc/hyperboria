import re

from aiosumma.parser.elements import (
    Group,
    Minus,
    Plus,
    Range,
    SearchField,
    Word,
)
from aiosumma.tree_transformers import (
    ContextWordTreeTransformer,
    ValuePredicateWordTreeTransformer,
    ValueWordTreeTransformer,
)
from aiosumma.tree_transformers.base import TreeTransformer
from izihawa_nlptools.regex import ISBN_REGEX

scimag_word_transformer = ContextWordTreeTransformer(
    node_value={'🔬', '⚗️'},
    context_transform=lambda context: context.index_aliases.append('scimag'),
)

scitech_word_transformer = ContextWordTreeTransformer(
    node_value={'📚', '📕', '📖'},
    context_transform=lambda context: context.index_aliases.append('scitech'),
)


class ExplainWordTransformer(ValueWordTreeTransformer):
    def __init__(self):
        super().__init__(node_value='🔑')

    def transform(self, node, context, parents, predicate_result):
        context.explain = True
        return None


explain_word_transformer = ExplainWordTransformer()


class YearWordTransformer(ValuePredicateWordTreeTransformer):
    def node_predicate(self, node):
        return re.match(r'^\d{4}$', node.value)

    def is_single_member_of_group(self, parents):
        return parents and isinstance(parents[-1], Group) and len(parents[-1]) == 1

    def transform(self, node, context, parents, predicate_result):
        year = int(node.value)
        if not parents or self.is_single_member_of_group(parents):
            return node
        if 1800 < year < 2100:
            context.set_query_point_of_time(year=year)
        return node


class EditionWordTransformer(ValuePredicateWordTreeTransformer):
    def node_predicate(self, node):
        return re.match(r'^(\d+)(st|nd|rd|th)$', node.value)

    def transform(self, node, context, parents, predicate_result):
        edition = predicate_result.group(1)
        if 1 <= int(edition) < 50:
            return SearchField('edition', Word(edition))
        return node


class IsbnWordTransformer(ValuePredicateWordTreeTransformer):
    def node_predicate(self, node):
        return re.match(ISBN_REGEX, node.value)

    def transform(self, node, context, parents, predicate_result):
        isbn = predicate_result[0].replace('-', '')
        context.is_exploration = False
        return SearchField('isbns', Word(isbn))


class LanguageWordTransformer(ValuePredicateWordTreeTransformer):
    languages = {
        '🇪🇹': 'am',
        '🇦🇪': 'ar',
        '🇩🇪': 'de',
        '🇬🇧': 'en',
        '🏴󠁧󠁢󠁥󠁮󠁧󠁿': 'en',
        '🇪🇸': 'es',
        '🇮🇷': 'fa',
        '🇮🇳': 'hi',
        '🇮🇩': 'id',
        '🇮🇹': 'it',
        '🇯🇵': 'ja',
        '🇲🇾': 'ms',
        '🇧🇷': 'pb',
        '🇷🇺': 'ru',
        '🇹🇯': 'tg',
        '🇺🇦': 'uk',
        '🇺🇿': 'uz',
    }

    def node_predicate(self, node):
        return node.value in self.languages

    def transform(self, node, context, parents, predicate_result):
        return SearchField('language', Word(self.languages[node.value]))
