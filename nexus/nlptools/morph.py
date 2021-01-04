import math

import lemminflect  # noqa
import pymorphy2
import spacy


class EnglishMorphology:
    VERBS = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}
    ADJS = {'JJ', 'JJR', 'JJS'}
    NOUNS = {'NN', 'NNP', 'NNPS', 'NNS'}
    ADVERBS = {'RB', 'RBR', 'RBS'}

    WORD_KINDS = [VERBS, ADJS, NOUNS, ADVERBS]

    def __init__(self, name):
        self.nlp = spacy.load(name)

    def derive_forms(self, word):
        forms = set()
        word = self.nlp(word)[0]
        inflected = False
        for kind in self.WORD_KINDS:
            if word.tag_ in kind:
                for w in kind:
                    inflection = word._.inflect(w)
                    if inflection:
                        inflected = True
                        forms.add(word._.inflect(w))
        if not inflected and word:
            forms.add(str(word))
        return list(sorted(forms))


class RussianMorphology:
    def __init__(self):
        self.morph_analyzer = pymorphy2.MorphAnalyzer()

    def derive_forms(self, word):
        words = set()
        phrase_word_form = self.morph_analyzer.parse(word)[0]
        for lexeme in phrase_word_form.lexeme:
            if lexeme.word == word:
                coef = 1.0
            else:
                coef = 1.0 / math.log1p(len(phrase_word_form.lexeme))
            if 'Abbr' in lexeme.tag:
                continue
            words.add(f'{lexeme.word}^{coef:.2f}')
        return list(sorted(words))
