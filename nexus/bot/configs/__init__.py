from izihawa_utils import env
from library.configurator import Configurator


def get_config():
    return Configurator([
        'nexus/bot/configs/base.yaml',
        'nexus/bot/configs/metrics.yaml?',
        'nexus/bot/configs/%s.yaml?' % env.type,
        'nexus/bot/configs/logging.yaml',
        'nexus/bot/configs/promotions.yaml',
    ])


config = get_config()
