import cld3


def detect_language(text: str) -> str:
    prediction = cld3.get_language(text)
    if prediction and prediction.is_reliable:
        if prediction.language.endswith('-Latn'):
            return prediction.language[:2]
        return prediction.language
