from izihawa_utils import env
from library.configurator import Configurator


def get_config():
    return Configurator([
        'nexus/hub/configs/base.yaml',
        'nexus/hub/configs/%s.yaml?' % env.type,
        'nexus/hub/configs/logging.yaml',
    ])


config = get_config()
