import asyncio
import base64
import datetime
import io
import time

import lightgbm as lgbm
import numpy as np
from nexus.nlptools.language_detect import detect_language

from .base import Rescorer

# ToDo: deduplicate code


def convert_scoring_to_vec_current_version(
    original_score,
    schema_id,
    document_age,
    downloads_count,
    ref_by_count,
    same_language,
    same_query_language,
    query_tokens_count,
    query_documents_similarity_vector,
):
    return np.array([
        original_score,
        schema_id,
        document_age,
        downloads_count,
        ref_by_count,
        same_language,
        same_query_language,
        query_tokens_count,
    ] + query_documents_similarity_vector)


def convert_scoring_to_vec_future_version(
    doc_id,
    original_score,
    schema_id,
    document_age,
    downloads_count,
    ref_by_count,
    same_language,
    same_query_language,
    query_tokens_count,
    query_documents_similarity_vector,
):
    return np.array([
        doc_id,
        original_score,
        schema_id,
        document_age,
        downloads_count,
        ref_by_count,
        same_language,
        same_query_language,
        query_tokens_count,
    ] + query_documents_similarity_vector)


def schema_to_id(schema):
    return 1 if schema == 'scimag' else 2


def query_document_similarity_measures(query_tokens, query_tokens_set, query_tokens_count, document_tokens):
    max_longest_sequence_not_ordered = 0
    min_sequence_not_ordered = 1024
    current_longest_sequence_not_ordered = 0
    two_grams_not_ordered = 0
    last_token = -1
    for token_ix, token in enumerate(document_tokens):
        if token in query_tokens_set:
            if last_token != -1:
                min_sequence_not_ordered = min(min_sequence_not_ordered, token_ix - last_token)
                if token_ix - last_token == 1:
                    two_grams_not_ordered += 1
            last_token = token_ix
            current_longest_sequence_not_ordered += 1
        else:
            current_longest_sequence_not_ordered = 0
        max_longest_sequence_not_ordered = max(
            max_longest_sequence_not_ordered,
            current_longest_sequence_not_ordered,
        )
    return [
        max_longest_sequence_not_ordered,
        min_sequence_not_ordered,
        two_grams_not_ordered,
        float(max_longest_sequence_not_ordered) / (float(query_tokens_count) + 1.0),
        float(two_grams_not_ordered) / (float(query_tokens_count) + 1.0),
    ]


def cast_issued_at(document):
    if 'issued_at' in document:
        try:
            return datetime.date.fromtimestamp(document['issued_at'])
        except ValueError:
            return datetime.date(2000, 1, 1)
    else:
        return datetime.date(2000, 1, 1)


def calculate_title_tokens(document):
    # ToDo: should we add tags?
    title_tokens = list(document.get('authors', []))
    if document.get('title'):
        title_tokens.append(document['title'])
    return (' '.join(title_tokens)).lower().split()


class ClassicRescorer(Rescorer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lgbm_ranker = lgbm.Booster(model_file='nexus/meta_api/models/classic.txt')

    def write_to_log_future_version(self, session_id, scored_documents, query, now, language):
        future_scoring_vecs = []

        query_language = detect_language(query)
        query_tokens_count = query.count(' ')
        query_tokens = query.lower().strip('"\'”`').split()
        query_tokens_set = set(query_tokens)

        for scored_document in scored_documents:
            document = scored_document['document']
            original_id = document.get('original_id') or document['id']

            title_tokens = calculate_title_tokens(document)

            query_documents_similarity_vector = query_document_similarity_measures(
                query_tokens,
                query_tokens_set,
                query_tokens_count,
                title_tokens,
            )
            future_scoring_vecs.append(convert_scoring_to_vec_future_version(
                doc_id=original_id,
                original_score=scored_document['score'],
                schema_id=schema_to_id(scored_document['schema']),
                document_age=(now - cast_issued_at(document)).total_seconds(),
                downloads_count=scored_document['document'].get('downloads_count', 0),
                ref_by_count=document.get('ref_by_count', 0),
                same_language=int(language == document.get('language')),
                same_query_language=int(query_language == document.get('language')),
                query_tokens_count=query_tokens_count,
                query_documents_similarity_vector=query_documents_similarity_vector
            ))

        data = io.BytesIO()
        np.savez_compressed(data, future_scoring_vecs, allow_pickle=True)
        data = base64.b64encode(data.getvalue()).decode()

        log_entry = {
            'action': 'search',
            'scorings': data,
            'session_id': session_id,
            'unixtime': time.time(),
            'version': 4,
            'vertical': 'classic',
        }

        self.learn_logger.info(log_entry)

    def _rescore(self, session_id, scored_documents, query, now, language):
        current_scoring_vecs = []

        query_language = detect_language(query)
        query_tokens_count = query.count(' ')
        query_tokens = query.lower().strip('"\'”`').split()
        query_tokens_set = set(query_tokens)

        for scored_document in scored_documents:
            # ToDo: Use shared wrappers
            document = scored_document['document']

            title_tokens = calculate_title_tokens(document)
            query_documents_similarity_vector = query_document_similarity_measures(
                query_tokens,
                query_tokens_set,
                query_tokens_count,
                title_tokens,
            )
            current_scoring_vecs.append(convert_scoring_to_vec_current_version(
                original_score=scored_document['score'],
                schema_id=schema_to_id(scored_document['schema']),
                document_age=(now - cast_issued_at(document)).total_seconds(),
                downloads_count=scored_document['document'].get('downloads_count', 0),
                ref_by_count=document.get('ref_by_count', 0),
                same_language=int(language == document.get('language')),
                same_query_language=int(query_language == document.get('language')),
                query_tokens_count=query_tokens_count,
                query_documents_similarity_vector=query_documents_similarity_vector,
            ))

        scores = self.lgbm_ranker.predict(current_scoring_vecs)
        for score, scored_document in zip(scores, scored_documents):
            scored_document['score'] = score

        scored_documents = sorted(scored_documents, key=lambda x: x['score'], reverse=True)
        for position, scored_document in enumerate(scored_documents):
            scored_document['position'] = position
        return scored_documents

    async def rescore(self, scored_documents, query, session_id, language):
        if not scored_documents:
            return scored_documents

        now = datetime.date.today()

        if self.learn_logger:
            # Needed due to bug in uvloop
            async def nested():
                await asyncio.get_running_loop().run_in_executor(
                    self.executor,
                    self.write_to_log_future_version,
                    session_id,
                    scored_documents,
                    query,
                    now,
                    language,
                )
            asyncio.create_task(nested())

        return await asyncio.get_running_loop().run_in_executor(
            self.executor,
            self._rescore,
            session_id,
            scored_documents,
            query,
            now,
            language,
        )
