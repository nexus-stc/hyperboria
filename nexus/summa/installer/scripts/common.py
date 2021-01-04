import os


def resolve_path(filepath):
    if os.path.isabs(filepath):
        return filepath
    cwd = os.environ.get('BUILD_WORKING_DIRECTORY', os.getcwd())
    filepath = os.path.join(cwd, filepath)
    return filepath
