from nexus.meta_api.query_extensions.grammar import (
    FieldResolver,
    MorphyResolver,
    OrOperation,
    UnknownOperationResolver,
    parser,
)

from . import checks
from .checks import QueryClass


class QueryProcessor:
    checks = tuple()

    def process(self, query, language):
        raise NotImplementedError()


class ClassicQueryProcessor(QueryProcessor):
    checks = (checks.check_doi, checks.check_isbn, checks.check_nid, checks.check_url)

    def process(self, query, language):
        uor = UnknownOperationResolver(OrOperation)
        fr = FieldResolver()
        morphy = MorphyResolver(language)
        for c in self.checks:
            r = c(query)
            if r:
                return r
        return {'query': str(uor.visit(fr.visit(morphy.visit(parser.parse(query))))), 'class': QueryClass.Default}
