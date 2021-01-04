from nexus.nlptools.utils import (
    cast_string_to_single_string,
    despace,
    remove_hashtags,
)


def test_cast_string_to_single_string():
    assert cast_string_to_single_string('kek kek 123\nkek') == 'kek-kek-123-kek'


def test_despace():
    assert despace(
        'ArXiv Papers Related   to Computer Science,  AI , Deep Learning, Computer Vision, NLP, etc\n\n\n'
        'From: @ai_python'
    ) == 'ArXiv Papers Related to Computer Science, AI , Deep Learning, Computer Vision, NLP, etc\nFrom: @ai_python'


def test_remove_hashtags():
    assert remove_hashtags('#ny riot') == ' riot'
