from izihawa_utils import env
from library.configurator import Configurator


def get_config():
    return Configurator([
        'nexus/pylon/configs/pylon.yaml',
    ], env_prefix='NEXUS_PYLON')


config = get_config()
