import re


class TextCollector:
    def __init__(self, inverted=False):
        self.text = []
        self.operations = []
        self.inverted = inverted

    def add_piece(self, text, operation):
        if self.inverted:
            self.text = [text] + self.text
            self.operations = [operation] * len(text) + self.operations
        else:
            self.text.append(text)
            self.operations.extend([operation] * len(text))

    def match(self, pattern):
        operations = []
        texts = []
        for match in re.finditer(pattern, ''.join(self.text)):
            left, right = match.span()
            texts.append(match.group())
            operations.extend(self.operations[left:right])
        return '\n'.join(texts), list(sorted(set(operations)))

    def clear(self):
        self.text = []
        self.operations = []
