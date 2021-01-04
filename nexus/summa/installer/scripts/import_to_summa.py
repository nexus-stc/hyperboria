import os
import shutil
import tarfile

import yaml
from izihawa_utils.file import mkdir_p

from .common import resolve_path


def import_to_summa(store_filepath, index_filepath, schema_filepath, database_path):
    store_filepath = resolve_path(store_filepath)
    index_filepath = resolve_path(index_filepath)
    schema_filepath = resolve_path(schema_filepath)
    database_path = resolve_path(database_path)

    mkdir_p(os.path.join(database_path, 'schema'))
    mkdir_p(os.path.join(database_path, 'index'))
    shutil.copy(schema_filepath, os.path.join(database_path, 'schema', os.path.basename(schema_filepath)))
    with open(schema_filepath, 'r') as f:
        database_path = os.path.join(database_path, 'index', yaml.safe_load(f)['name'])

    with tarfile.open(store_filepath) as f:
        f.extractall(database_path)
    with tarfile.open(index_filepath) as f:
        f.extractall(database_path)
