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

    def __str__(self):
        return "\n".join(str(stmt) for stmt in self.statements)

class LetStatement(Statement):
    def __init__(self, token, name, value):
        self.token = token
        self.name = name
        self.value = value

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return f"{self.token_literal()} {self.name} = {self.value};"

class Identifier(Expression):
    def __init__(self, token, value):
        self.token = token
        self.value = value

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return self.value