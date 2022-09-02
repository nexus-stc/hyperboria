import time
from typing import (
    Callable,
    Union,
)

from izihawa_utils.exceptions import BaseError
from library.telegram.common import close_button
from telethon.errors import MessageIdInvalidError


class ProgressBarLostMessageError(BaseError):
    pass


bars = {
    'filled': '█',
    'empty': ' ',
}


def percent(done, total):
    return min(float(done) / total, 1.0)


class ProgressBar:
    def __init__(
        self,
        telegram_client,
        request_context,
        banner,
        header,
        tail_text,
        message=None,
        source=None,
        throttle_secs: float = 0,
    ):
        self.telegram_client = telegram_client
        self.request_context = request_context
        self.banner = banner
        self.header = header
        self.tail_text = tail_text
        self.message = message
        self.source = source
        self.done = 0
        self.total = 1
        self.throttle_secs = throttle_secs

        self.last_text = None
        self.last_call = 0

    def share(self):
        if self.total > 0:
            return f'{float(percent(self.done, self.total) * 100):.1f}%'
        else:
            return f'{float(self.done / (1024 * 1024)):.1f}Mb'

    def _set_progress(self, done, total):
        self.done = done
        self.total = total

    def set_source(self, source):
        self.source = source

    async def render_banner(self):
        banner = self.banner.format(source=self.source)
        return f'`{self.header}\n{banner}`'

    async def render_progress(self):
        total_bars = 20
        progress_bar = ''
        if self.total > 0:
            filled = int(total_bars * percent(self.done, self.total))
            progress_bar = '|' + filled * bars['filled'] + (total_bars - filled) * bars['empty'] + '| '

        tail_text = self.tail_text.format(source=self.source)
        return f'`{self.header}\n{progress_bar}{self.share()} {tail_text}`'

    async def send_message(self, text, ignore_last_call=False):
        now = time.time()
        if not ignore_last_call and abs(now - self.last_call) < self.throttle_secs:
            return
        try:
            if not self.message:
                self.message = await self.telegram_client.send_message(
                    self.request_context.chat.chat_id,
                    text,
                    buttons=[close_button()],
                )
            elif text != self.last_text:
                r = await self.message.edit(text, buttons=[close_button()])
                if not r:
                    raise ProgressBarLostMessageError()
        except MessageIdInvalidError:
            raise ProgressBarLostMessageError()
        self.last_text = text
        self.last_call = now
        return self.message

    async def show_banner(self):
        return await self.send_message(await self.render_banner(), ignore_last_call=True)

    async def callback(self, done, total):
        self._set_progress(done, total)
        return await self.send_message(await self.render_progress())


class ThrottlerWrapper:
    def __init__(self, callback: Callable, throttle_secs: Union[int, float]):
        self.callback = callback
        self.last_call = 0
        self.throttle_secs = throttle_secs

    async def __call__(self, *args, **kwargs):
        now = time.time()
        if abs(now - self.last_call) < self.throttle_secs:
            return
        self.last_call = now
        return await self.callback(*args, **kwargs)
