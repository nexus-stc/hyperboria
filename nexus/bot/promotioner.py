import random


class Promotioner:
    """
    Promotioner is used to select promotion randomly based on weights of every promotion.
    """
    def __init__(self, promotions: list[dict]):
        self.promotions = promotions
        self.partial_sums: list = [self.promotions[0]['weight']]
        for promotion in self.promotions[1:]:
            self.partial_sums.append(promotion['weight'] + self.partial_sums[-1])

    def choose_promotion(self, language: str = 'en') -> str:
        pivot = random.randrange(self.partial_sums[-1])
        for partial_sum, promotion in zip(self.partial_sums, self.promotions):
            if partial_sum <= pivot:
                continue
            if language in promotion['texts']:
                return promotion['texts'][language]
            return promotion['texts']['en']
