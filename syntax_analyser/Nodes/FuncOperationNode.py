from lexical_analyser.token import Token


class FuncOperationNode:
    def __init__(self, func: Token, operands):
        self.func = func
        self.operands = operands
