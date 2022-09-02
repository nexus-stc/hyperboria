import random


class Promotioner:
    """
    Promotioner is used to select promotion randomly based on weights of every promotion.
    """
    def __init__(self, promotions: list[dict], default_promotion_index: int = 0):
        self.promotions = promotions
        self.default_promotion_index = default_promotion_index
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
            elif promotion.get('local', False):
                default_promotion = self.promotions[self.default_promotion_index]
                if language in default_promotion['texts']:
                    return default_promotion['texts'][language]
                return default_promotion['texts']['en']
            else:
                return promotion['texts']['en']
