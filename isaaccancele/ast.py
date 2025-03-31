# isaaccancele/ast.py
from typing import List

class Node:
    def token_literal(self) -> str:
        raise NotImplementedError()

class Statement(Node):
    pass

class Expression(Node):
    pass

class Program(Node):
    def __init__(self):
        self.statements: List[Statement] = []

    def token_literal(self):
        if self.statements:
            return self.statements[0].token_literal()
        return ""

class LetStatement(Statement):
    def __init__(self, token, name, value):
        self.token = token            # TokenType.LET
        self.name = name              # Identifier
        self.value = value            # Expression

    def token_literal(self):
        return self.token.literal

class Identifier(Expression):
    def __init__(self, token, value):
        self.token = token            # TokenType.IDENT
        self.value = value

    def token_literal(self):
        return self.token.literal
