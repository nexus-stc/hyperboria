from izihawa_configurator import Configurator
from izihawa_utils import env


def get_config():
    return Configurator([
        'idm/api/configs/base.yaml',
        'idm/api/configs/%s.yaml?' % env.type,
        'idm/api/configs/logging.yaml',
    ], env_prefix='IDM_API')


config = get_config()
