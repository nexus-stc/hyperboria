import logging
import traceback
from contextlib import asynccontextmanager
from typing import (
    Awaitable,
    Callable,
    Optional,
)

from telethon import (
    errors,
    events,
)

from .base import RequestContext


@asynccontextmanager
async def safe_execution(
    request_context: RequestContext,
    on_fail: Optional[Callable[[], Awaitable]] = None,
):
    try:
        try:
            yield
        except events.StopPropagation:
            raise
        except (
            errors.UserIsBlockedError,
            errors.QueryIdInvalidError,
            errors.MessageDeleteForbiddenError,
            errors.MessageIdInvalidError,
            errors.MessageNotModifiedError,
            errors.ChatAdminRequiredError,
        ) as e:
            request_context.error_log(e, level=logging.WARNING)
        except Exception as e:
            traceback.print_exc()
            request_context.error_log(e)
            if on_fail:
                await on_fail()
    except events.StopPropagation:
        raise
    except Exception as e:
        request_context.error_log(e)
