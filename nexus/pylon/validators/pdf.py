import hashlib
import logging
from io import BytesIO
from typing import Dict

import PyPDF2
from nexus.pylon.exceptions import BadResponseError
from nexus.pylon.pdftools import is_pdf
from nexus.pylon.validators.base import BaseValidator
from PyPDF2.errors import PdfReadError


class PdfValidator(BaseValidator):
    def __init__(self, params: Dict):
        super().__init__(params)
        self.md5 = params.get('md5')
        self.file = bytes()
        self.v = hashlib.md5()

    def update(self, chunk):
        self.file += chunk
        if self.md5:
            self.v.update(chunk)

    def validate(self):
        if self.md5 and self.md5.lower() == self.v.hexdigest().lower():
            logging.getLogger('nexus_pylon').debug({
                'action': 'validation',
                'mode': 'pylon',
                'result': 'md5_ok',
                'params': self.params,
            })
            return
        elif not is_pdf(f=self.file):
            logging.getLogger('nexus_pylon').debug({
                'action': 'validation',
                'mode': 'pylon',
                'result': 'not_pdf',
                'params': self.params,
            })
            raise BadResponseError(file=str(self.file[:100]))

        try:
            PyPDF2.PdfReader(BytesIO(self.file))
        except PdfReadError:
            logging.getLogger('nexus_pylon').debug({
                'action': 'validation',
                'mode': 'pylon',
                'result': 'not_opened_as_pdf',
                'params': self.params,
            })
            raise BadResponseError(file=str(self.file[:100]))
        logging.getLogger('nexus_pylon').debug({
            'action': 'validation',
            'mode': 'pylon',
            'result': 'ok',
            'params': self.params,
        })
