import asyncio
import logging

import uvloop
from aiosumma import (
    QueryProcessor,
    SummaClient,
)
from aiosumma.parser.elements import (
    Range,
    SearchField,
)
from aiosumma.text_transformers import (
    CleanTextTransformer,
    DespaceTextTransformer,
    LowerTextTransformer,
    UnmatchedParenthesesTextTransformer,
)
from aiosumma.tree_transformers import (
    DoiTreeTransformer,
    DoiWildcardWordTreeTransformer,
    ExactMatchTreeTransformer,
    FieldTreeTransformer,
    MorphyTreeTransformer,
    OptimizingTreeTransformer,
    OrderByTreeTransformer,
    SynonymTreeTransformer,
    TantivyTreeTransformer,
    ValuesWordTreeTransformer,
)
from library.aiogrpctools import AioGrpcServer
from library.logging import configure_logging
from nexus.meta_api.configs import get_config
from nexus.meta_api.providers.stat import StatProvider
from nexus.meta_api.services.documents import DocumentsService
from nexus.meta_api.services.search import SearchService
from nexus.meta_api.word_transformers import (
    EditionWordTransformer,
    IsbnWordTransformer,
    LanguageWordTransformer,
    YearWordTransformer,
    explain_word_transformer,
    scimag_word_transformer,
    scitech_word_transformer,
)


def create_query_transformer(valid_fields, invalid_fields, order_by_valid_fields):
    return QueryProcessor(
        tree_transformers=[
            OrderByTreeTransformer(
                field_aliases={
                    'date': 'issued_at',
                    'page': 'pages',
                    'pr': 'page_rank',
                    'refc': 'referenced_by_count',
                },
                valid_fields=frozenset(order_by_valid_fields)
            ),
            FieldTreeTransformer(
                field_aliases={
                    'author': 'authors',
                    'body': 'content',
                    'date': 'issued_at',
                    'ipfs': 'ipfs_multihashes',
                    'isbn': 'isbns',
                    'issn': 'issns',
                    'format': 'extension',
                    'journal': 'container_title',
                    'lang': 'language',
                    'page': 'pages',
                    'pr': 'page_rank',
                    'refc': 'referenced_by_count',
                    'refs': 'references',
                },
                valid_fields=frozenset(valid_fields),
                invalid_fields=frozenset(invalid_fields),
            ),
            ValuesWordTreeTransformer(
                word_transformers=[
                    YearWordTransformer(),
                    EditionWordTransformer(),
                    LanguageWordTransformer(),
                    DoiWildcardWordTreeTransformer(),
                    IsbnWordTransformer(),
                ],
                ignore_nodes=(Range, SearchField),
            ),
            DoiTreeTransformer(score='3.0'),
            ExactMatchTreeTransformer('title'),
            MorphyTreeTransformer(ignore_nodes=(SearchField,)),
            SynonymTreeTransformer.drugs(),
            TantivyTreeTransformer(),
            OptimizingTreeTransformer(),
        ]
    )


class GrpcServer(AioGrpcServer):
    def __init__(self, config):
        self.log_config(config)
        super().__init__(address=config['grpc']['host'], port=config['grpc']['port'])
        self.config = config

        self.stat_provider = StatProvider(stat_provider_config=self.config['stat_provider'])

        self.query_preprocessor = QueryProcessor(
            text_transformers=[
                DespaceTextTransformer(),
                LowerTextTransformer(),
                CleanTextTransformer(),
                UnmatchedParenthesesTextTransformer(),
            ],
            tree_transformers=[
                ValuesWordTreeTransformer(
                    word_transformers=[
                        explain_word_transformer,
                        scimag_word_transformer,
                        scitech_word_transformer,
                    ],
                    ignore_nodes=(Range, SearchField),
                )
            ],
        )

        scimag_fields = {
            'id', 'abstract', 'authors', 'container_title', 'content',
            'doi', 'ipfs_multihashes', 'issns', 'isbns', 'issued_at', 'language', 'original_id',
            'page_rank', 'referenced_by_count', 'references', 'tags', 'title', 'year',
        }
        order_by_scimag_fields = {
            'id',
            'referenced_by_count',
            'issued_at',
            'page_rank',
            'updated_at'
        }
        scitech_fields = {
            'id', 'authors', 'doi', 'description', 'extension',
            'ipfs_multihashes', 'isbns', 'issued_at', 'language', 'original_id', 'pages',
            'tags', 'title', 'updated_at', 'year',
        }
        order_by_scitech_fields = {
            'id',
            'issued_at',
            'pages',
            'updated_at'
        }

        self.query_transformers = {
            'scimag': create_query_transformer(
                valid_fields=scimag_fields,
                invalid_fields=scitech_fields.difference(scimag_fields),
                order_by_valid_fields=order_by_scimag_fields,
            ),
            'scitech': create_query_transformer(
                valid_fields=scitech_fields,
                invalid_fields=scimag_fields.difference(scitech_fields),
                order_by_valid_fields=order_by_scitech_fields,
            )
        }
        self.summa_client = SummaClient(
            endpoint=config['summa']['endpoint'],
            connection_timeout=config['summa']['connection_timeout'],
        )

        learn_logger = logging.getLogger('learn') if self.config['application']['learn_log'] else None

        self.search_service = SearchService(
            application=self,
            query_preprocessor=self.query_preprocessor,
            query_transformers=self.query_transformers,
            summa_client=self.summa_client,
            stat_provider=self.stat_provider,
            learn_logger=learn_logger,
        )
        self.documents_service = DocumentsService(
            application=self,
            query_preprocessor=self.query_preprocessor,
            query_transformers=self.query_transformers,
            summa_client=self.summa_client,
            stat_provider=self.stat_provider,
            learn_logger=learn_logger,
        )
        self.starts.extend([
            self.summa_client,
            self.stat_provider,
            self.search_service,
            self.documents_service,
        ])


def main():
    config = get_config()
    configure_logging(config)
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    grpc_server = GrpcServer(config)
    return loop.run_until_complete(grpc_server.start_and_wait())


if __name__ == '__main__':
    result = main()
    logging.getLogger('debug').debug({
        'action': 'exit',
        'mode': 'main',
        'result': str(result)
    })
