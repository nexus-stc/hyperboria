from library.configurator import Configurator


def get_config():
    return Configurator([
        'idm/api/configs/base.yaml',
        'idm/api/configs/logging.yaml',
    ], env_prefix='NEXUS_IDM_API')


config = get_config()
