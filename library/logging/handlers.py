import logging.handlers
import os
import queue

from izihawa_types.var import varstr


class QueueHandler(logging.handlers.QueueHandler):
    def __init__(self, *handlers):
        self._queue = queue.Queue(-1)
        self._listener = logging.handlers.QueueListener(self._queue, *handlers, respect_handler_level=True)
        self.setLevel('INFO')

        super().__init__(self._queue)
        self._listener.start()

    def stop(self):
        self._listener.stop()

    def prepare(self, record):
        return record


class BaseFileHandler(logging.handlers.WatchedFileHandler):
    def _open(self):
        file = super()._open()
        os.chmod(self.baseFilename, 0o644)
        return file


class BaseBinaryFileHandler(BaseFileHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, mode='ab+')

    def emit(self, record):
        try:
            self.stream.write(varstr(record.msg))
            self.flush()
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)
