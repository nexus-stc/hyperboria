from izihawa_configurator import Configurator
from izihawa_utils import env


def get_config():
    return Configurator([
        'nexus/bot/configs/base.yaml',
        'nexus/bot/configs/%s.yaml?' % env.type,
        'nexus/bot/configs/logging.yaml',
    ], env_prefix='NEXUS_BOT')


config = get_config()
