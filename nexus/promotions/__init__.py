from izihawa_configurator import Configurator


def get_promotions():
    return Configurator(['nexus/promotions/promotions.yaml'])['promotions']


promotions = get_promotions()
