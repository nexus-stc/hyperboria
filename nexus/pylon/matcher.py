import re


class Matcher:
    def __init__(self, param_regexes):
        self.param_regexes = param_regexes
        for param_regex in self.param_regexes:
            self.param_regexes[param_regex] = re.compile(self.param_regexes[param_regex])

    def is_match(self, params) -> bool:
        for param in params:
            if params[param]:
                if param_regex := self.param_regexes.get(param):
                    if re.match(param_regex, params[param]):
                        return True
        return False
