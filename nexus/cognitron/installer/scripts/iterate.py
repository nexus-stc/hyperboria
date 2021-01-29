import glob
import multiprocessing
import os
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


def _do_work(coder, chunk_size, limit, store_filepath):
    with open(store_filepath, 'rb') as file:
        data = file.read()
    print(f'Processing segment {store_filepath}, size: {len(data) / (1024 * 1024):.2f} Mb ...')
    tr = TantivyReader(data, coder=coder)
    for chunk_num, documents in enumerate(ichunks(tr.documents(), chunk_size)):
        for doc_num, document in enumerate(documents):
            if limit and chunk_num * chunk_size + doc_num > limit:
                print(f'Segment {store_filepath} early terminated due to limits')
                return
            work(document)
    print(f'Segment {store_filepath} successfully processed')


def iterate(data_filepath, schema_filepath, processes=8, chunk_size=100, limit=1):
    data_filepath = resolve_path(data_filepath)
    schema_filepath = resolve_path(schema_filepath)

    with open(schema_filepath) as schema_file:
        coder = TantivyCoder(yaml.safe_load(schema_file.read()))

    store_filepaths = glob.glob(os.path.join(data_filepath, '*.store'))

    print(f'Total segments: {len(store_filepaths)}')
    pool = multiprocessing.Pool(processes)
    pool.map(partial(_do_work, coder, chunk_size, limit), store_filepaths)
