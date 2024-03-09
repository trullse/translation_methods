from lexical_analyser.token import Token
from enum import Enum


class IdentifierType(Enum):
    BUILT_IN_FUNC = 'Built in function'
    VARIABLE = 'Variable'
    CONSTANT = 'Constant'


class ExpressionNode:
    def __init__(self, nodes: list):
        self.nodes = nodes
        self.return_type = None

    def __str__(self):
        return '[Expression node' + ', '.join(map(str, self.nodes)) + ']'

    def __repr__(self):
        return '[Expression node' + ', '.join(map(str, self.nodes)) + ']'

    def get_func(self):
        return self.nodes[0]

    def get_args(self):
        return [self.nodes[1:]]


class ConstantNode:
    def __init__(self, token: Token):
        self.pos = token.pos
        self.text = token.text
        self.value = token.value
        self.return_type = None

    def __str__(self):
        return f'[Constant node: pos: {self.pos}, text: {self.text}, value: {self.value}]'

    def __repr__(self):
        return f'[Constant node: pos: {self.pos}, text: {self.text}, value: {self.value}]'


class IdentifierNode:
    def __init__(self, token: Token):
        self.pos = token.pos
        self.text = token.text
        self.type = self.text_to_type(token.info)
        self.return_type = None

    def __str__(self):
        return f'[Identifier node: pos: {self.pos}, text: {self.text}, type: {self.type.value}]'

    def __repr__(self):
        return f'[Identifier node: pos: {self.pos}, text: {self.text}, type: {self.type.value}]'

    def text_to_type(self, info: str):
        if info in ('Logical symbol',
                     'Keyword',
                     'Arithmetic operator',
                     'Arithmetic function',
                     'String operator'):
            return IdentifierType.BUILT_IN_FUNC
        elif info == 'Identifier':
            return IdentifierType.VARIABLE
        elif info in ('Numeric constant',
                      'String constant'):
            return IdentifierType.CONSTANT
        else:
            raise Exception('Undefined token type')

