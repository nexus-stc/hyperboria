from nexus.meta_api.query_extensionner.grammar import (
    FieldResolver,
    UnknownOperationResolver,
    parser,
)


def test_parser():
    assert (
        str(parser.parse(
            '(hemoglobin- er OR hemoglobins-a) '
            'AND -fetal AND (human to monkey - is cool) '
            'AND year:[1992 to 1994]'
        )) == '(hemoglobin- er OR hemoglobins-a) AND -fetal AND (human to monkey is cool) AND year:[1992 TO 1994]'
    )
    assert (str(parser.parse("bek OR 'kek'")) == 'bek OR "kek"')
    assert (str(parser.parse("bek OR 'kek")) == 'bek OR kek')
    assert (str(parser.parse("bek OR a'kek")) == 'bek OR a kek')
    assert (str(parser.parse("bek' OR 'kek mek'")) == 'bek " OR " kek mek')

    assert (str(parser.parse("field:test")) == 'field:test')
    assert (str(parser.parse("field: test")) == 'field test')
    assert (str(parser.parse("field : test")) == 'field test')
    assert (str(parser.parse("field :test")) == 'field test')


def test_resolvers():
    def resolver(query):
        tree = parser.parse(query)
        return UnknownOperationResolver().visit(FieldResolver().visit(tree))

    assert str(resolver('kek -bek')) == 'kek AND -bek'
    assert str(resolver("Glass s OR Guide OR to OR Commercial OR Vehicles OR 1989")) == \
           'Glass OR s OR Guide OR to OR Commercial OR Vehicles OR 1989'
    assert str(resolver('bek OR kek')) == 'bek OR kek'
    assert str(resolver('bek kek')) == 'bek OR kek'
    assert str(resolver('title:(hemoglobin OR -fetal) OR abstract:"alpha-hemoglobin"')) == \
           'title:(hemoglobin OR -fetal) OR abstract:"alpha-hemoglobin"'
    # assert str(resolver('lumbar spinal [with]')) == ''
    # assert str(resolver('lumbar spinal [with consumer]')) == ''
    # assert str(resolver('lumbar spinal [with consumer summary]')) == ''
