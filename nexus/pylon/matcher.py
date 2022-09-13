import re
from typing import (
    List,
    Tuple,
)


class Matcher:
    def __init__(self, param_regexes):
        self.param_regexes = param_regexes
        for param_regex in self.param_regexes:
            self.param_regexes[param_regex] = re.compile(self.param_regexes[param_regex])

    def is_match(self, params) -> bool:
        for param in params:
            param_value = params[param]
            param_regex = self.param_regexes.get(param)
            if param_value and param_regex:
                if not isinstance(param_value, (List, Tuple)):
                    param_value = [param_value]
                for el in param_value:
                    if re.match(param_regex, el):
                        return el
