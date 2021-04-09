import asyncio

import uvloop
from library.logging import configure_logging
from nexus.bot.application import TelegramApplication
from nexus.bot.configs import get_config


def main(config):
    uvloop.install()
    configure_logging(config)
    if config['metrics']['enabled']:
        from library.metrics_server import MetricsServer
        MetricsServer(config['metrics']).fork_process()
    asyncio.get_event_loop().run_until_complete(TelegramApplication(config=config).start_and_wait())


if __name__ == '__main__':
    main(config=get_config())
