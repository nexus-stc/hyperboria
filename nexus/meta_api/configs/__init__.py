from izihawa_configurator import Configurator
from izihawa_utils import env


def get_config():
    return Configurator([
        'nexus/meta_api/configs/base.yaml',
        'nexus/meta_api/configs/%s.yaml?' % env.type,
        'nexus/meta_api/configs/logging.yaml',
    ], env_prefix='NEXUS_META_API')


config = get_config()
