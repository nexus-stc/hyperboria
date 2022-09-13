from typing import Dict


class BaseValidator:
    def __init__(self, params: Dict):
        self.params = params

    def update(self, chunk):
        pass

    def validate(self):
        pass
