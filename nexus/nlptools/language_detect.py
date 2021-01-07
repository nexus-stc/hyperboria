import cld3


def detect_language(text: str) -> str:
    prediction = cld3.get_language(text)
    if prediction and prediction.is_reliable:
        return prediction.language
