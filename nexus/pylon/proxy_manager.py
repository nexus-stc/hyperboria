import random
from typing import (
    Iterator,
    List,
    Optional,
    Set,
    Union,
)


class AllOf:
    def __init__(self, tags: Set):
        self.tags = tags

    def __str__(self):
        return f'AllOf({self.tags})'

    def __repr__(self):
        return f'AllOf({self.tags})'

    def match(self, target_tags):
        return self.tags.issubset(target_tags)


class AnyOf:
    def __init__(self, tags: Set):
        self.tags = tags

    def __str__(self):
        return f'AnyOf({self.tags})'

    def __repr__(self):
        return f'AnyOf({self.tags})'

    def match(self, target_tags):
        return not self.tags.isdisjoint(target_tags)


class Proxy:
    def __init__(self, proxy_config):
        self.address = proxy_config['address']
        self.name = proxy_config['name']
        self.tags = set(proxy_config.get('tags', []))

    def get_address(self):
        return self.address

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class ProxyManager:
    def __init__(self, proxies=None):
        if proxies is None:
            proxies = []
        self.proxies = [Proxy(proxy) for proxy in proxies]

    def get_proxy(self, tags: Optional[Union[AllOf, AnyOf, Set]] = None) -> Proxy:
        if tags:
            if isinstance(tags, set):
                tags = AllOf(tags)
            options = list(filter(lambda proxy: tags.match(proxy.tags), self.proxies))
            if options:
                return random.choice(options)
        else:
            return random.choice(self.proxies)

    def get_proxies(self, proxy_list: List[Union[AllOf, AnyOf, Set]]) -> Iterator:
        for proxy_tags in proxy_list:
            yield self.get_proxy(proxy_tags)

    def __str__(self):
        return f'ProxyManager({self.proxies})'
