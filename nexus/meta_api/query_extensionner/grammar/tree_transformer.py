from izihawa_utils.text import camel_to_snake
from nexus.nlptools.morph import (
    EnglishMorphology,
    RussianMorphology,
)

from .tree import (
    AndOperation,
    BaseOperation,
    Group,
    OrOperation,
    Unary,
    Word,
)


class TreeVisitor:
    visitor_method_prefix = 'visit_'
    generic_visitor_method_name = 'generic_visit'

    _get_method_cache = None

    def _get_method(self, node):
        if self._get_method_cache is None:
            self._get_method_cache = {}
        try:
            meth = self._get_method_cache[type(node)]
        except KeyError:
            for cls in node.__class__.mro():
                try:
                    method_name = "{}{}".format(
                        self.visitor_method_prefix,
                        camel_to_snake(cls.__name__)
                    )
                    meth = getattr(self, method_name)
                    break
                except AttributeError:
                    continue
            else:
                meth = getattr(self, self.generic_visitor_method_name)
            self._get_method_cache[type(node)] = meth
        return meth

    def visit(self, node, parents=None):
        """ Basic, recursive traversal of the tree. """
        parents = parents or []
        method = self._get_method(node)
        yield from method(node, parents)
        for child in node.children:
            yield from self.visit(child, parents + [node])

    def generic_visit(self, node, parents=None):
        """
        Default visitor function, called if nothing matches the current node.
        """
        return iter([])  # No-op


class TreeTransformer(TreeVisitor):
    def replace_node(self, old_node, new_node, parent):
        for k, v in parent.__dict__.items():  # pragma: no branch
            if v == old_node:
                parent.__dict__[k] = new_node
                break
            elif isinstance(v, list):
                try:
                    i = v.index(old_node)
                    if new_node is None:
                        del v[i]
                    else:
                        v[i] = new_node
                    break
                except ValueError:
                    pass  # this was not the attribute containing old_node
            elif isinstance(v, tuple):
                try:
                    i = v.index(old_node)
                    v = list(v)
                    if new_node is None:
                        del v[i]
                    else:
                        v[i] = new_node
                    parent.__dict__[k] = tuple(v)
                    break
                except ValueError:
                    pass  # this was not the attribute containing old_node

    def generic_visit(self, node, parent=None):
        return node

    def visit(self, node, parents=None):
        """
        Recursively traverses the tree and replace nodes with the appropriate
        visitor method's return values.
        """
        parents = parents or []
        method = self._get_method(node)
        new_node = method(node, parents)
        if parents:
            self.replace_node(node, new_node, parents[-1])
        node = new_node
        if node is not None:
            for child in node.children:
                self.visit(child, parents + [node])
        return node


class UnknownOperationResolver(TreeTransformer):
    VALID_OPERATIONS = frozenset([None, AndOperation, OrOperation])
    DEFAULT_OPERATION = OrOperation

    def __init__(self, resolve_to=None):
        if resolve_to not in self.VALID_OPERATIONS:
            raise ValueError("%r is not a valid value for resolve_to" % resolve_to)
        self.resolve_to = resolve_to
        self.last_operation = {}

    def _first_nonop_parent(self, parents):
        for parent in parents:
            if not isinstance(parent, BaseOperation):
                return id(parent)  # use id() because parent might not be hashable
        return None

    def visit_or_operation(self, node, parents=None):
        if self.resolve_to is None:
            # memorize last op
            parent = self._first_nonop_parent(parents)
            self.last_operation[parent] = OrOperation
        return node

    def visit_and_operation(self, node, parents=None):
        if self.resolve_to is None:
            # memorize last op
            parent = self._first_nonop_parent(parents)
            self.last_operation[parent] = AndOperation
        return node

    def visit_unknown_operation(self, node, parents=None):
        # resolve
        if any(map(lambda x: isinstance(x, Unary), node.operands)):
            operation = AndOperation
        elif self.resolve_to is not None:
            operation = self.resolve_to
        else:
            parent = self._first_nonop_parent(parents)
            operation = self.last_operation.get(parent, None)
            if operation is None:
                operation = self.DEFAULT_OPERATION
        return operation(*node.operands)


class FieldResolver(TreeTransformer):
    FIELD_ALIASES = {
        'author': 'authors',
        'isbn': 'isbns',
        'journal': 'container_title',
        'lang': 'language',
    }
    VALID_FIELDS = frozenset([
        'id', 'abstract', 'authors', 'container_title',
        'doi', 'description', 'isbns', 'issued_at', 'language', 'original_id',
        'references', 'tags', 'title', 'year',
    ])

    def visit_search_field(self, node, parents=None):
        if node.name in self.FIELD_ALIASES:
            node.name = self.FIELD_ALIASES[node.name]

        if node.name not in self.VALID_FIELDS:
            return OrOperation(Word(node.name), node.expr)

        return node


class MorphyResolver(TreeTransformer):
    morphology = {
        'ru': RussianMorphology(),
        'en': EnglishMorphology('en_core_web_sm'),
    }

    def __init__(self, language, is_morph=False, is_accent=True):
        super().__init__()
        self.language = language
        self.is_morph = is_morph
        self.is_accent = is_accent

    def has_morphy_condition(self, node):
        return (
            (isinstance(node, BaseOperation)
                and len(node.operands) <= 2
                and all(map(lambda x: isinstance(x, Word), node.operands)))
            or isinstance(node, Word)
        )

    def morph(self, node, parents=None):
        if self.has_morphy_condition(node):
            return self.visit(node, parents)
        return node

    def visit_word(self, node, parents=None):
        node.value = node.value.lower()
        if node.final or self.language not in self.morphology:
            return node
        if self.is_morph:
            forms = [Word(w, final=True) for w in self.morphology[self.language].derive_forms(node.value)]
            return Group(OrOperation(*forms))
        if self.is_accent:
            if 'ё' in node.value:
                forms = [Word(node.value, final=True), Word(node.value.replace('ё', 'е'), final=True)]
                return Group(OrOperation(*forms))
        return node
