import multiprocessing
import tarfile
from functools import partial

import yaml
from izihawa_utils.itertools import ichunks
from tantipy import (
    TantivyCoder,
    TantivyReader,
)

from .common import resolve_path


def work(document):
    # ToDo: Replace this function to what you want to do with document
    print(document)


def _do_work(coder, filepath, chunk_size, limit, member):
    with tarfile.open(filepath, 'r') as tar_file:
        file = tar_file.extractfile(member)
        data = file.read()
        print(f'Processing segment {member.name}, size: {len(data) / (1024 * 1024):.2f} Mb ...')
        tr = TantivyReader(data, coder=coder)
        for chunk_num, documents in enumerate(ichunks(tr.documents(), chunk_size)):
            for doc_num, document in enumerate(documents):
                if chunk_num * chunk_size + doc_num > limit:
                    print(f'Segment {member.name} early terminated due to limits')
                    return
                work(document)
        print(f'Segment {member.name} successfully processed')


def iterate(store_filepath, schema_filepath, processes=8, chunk_size=100, limit=1):
    store_filepath = resolve_path(store_filepath)
    schema_filepath = resolve_path(schema_filepath)

    with open(schema_filepath) as schema_file:
        coder = TantivyCoder(yaml.safe_load(schema_file.read()))

    with tarfile.open(store_filepath, 'r') as tar_file:
        members = []
        for member in tar_file.getmembers():
            if not member.name.endswith('store'):
                continue
            members.append(member)

    print(f'Total segments: {len(members)}')
    pool = multiprocessing.Pool(processes)
    pool.map(partial(_do_work, coder, store_filepath, chunk_size, limit), members)
