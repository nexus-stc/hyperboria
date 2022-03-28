import lemminflect  # noqa
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
