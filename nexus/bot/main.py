import asyncio

import uvloop
from library.logging import configure_logging
from nexus.bot.application import TelegramApplication
from nexus.bot.configs import get_config


def main(config):
    configure_logging(config)
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(TelegramApplication(config=config).start_and_wait())


if __name__ == '__main__':
    main(config=get_config())
