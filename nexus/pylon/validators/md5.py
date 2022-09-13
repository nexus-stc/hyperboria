import hashlib
from typing import Dict

from nexus.pylon.exceptions import IncorrectMD5Error
from nexus.pylon.validators.base import BaseValidator


class Md5Validator(BaseValidator):
    def __init__(self, params: Dict):
        super().__init__(params)
        self.md5 = params['md5']
        self.v = hashlib.md5()

    def update(self, chunk: bytes):
        self.v.update(chunk)

    def validate(self):
        digest = self.v.hexdigest()
        if self.md5.lower() != digest.lower():
            raise IncorrectMD5Error(requested_md5=self.md5, downloaded_md5=digest)
