from izihawa_configurator import Configurator
from izihawa_utils import env


def get_config():
    return Configurator([
        'nexus/hub/configs/base.yaml',
        'nexus/hub/configs/%s.yaml?' % env.type,
        'nexus/hub/configs/pylon.yaml',
        'nexus/hub/configs/logging.yaml',
    ], env_prefix='NEXUS_HUB')


config = get_config()
