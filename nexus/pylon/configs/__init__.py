from izihawa_configurator import Configurator


def get_config():
    return Configurator([
        'nexus/pylon/configs/pylon.yaml',
    ], env_prefix='NEXUS_PYLON')


config = get_config()
