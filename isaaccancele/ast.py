from typing import List

class Node:
    def token_literal(self):
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

# ========== STATEMENTS ==========

class LetStatement(Statement):
    def __init__(self, token, name, value):
        self.token = token        # token 'let'
        self.name = name          # Identifier
        self.value = value        # Expression

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return f"{self.token_literal()} {self.name} = {self.value};"

class ExpressionStatement(Statement):
    def __init__(self, token, expression):
        self.token = token
        self.expression = expression

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return str(self.expression)

# ========== EXPRESSIONS ==========

class Identifier(Expression):
    def __init__(self, token, value):
        self.token = token      # token IDENT
        self.value = value      # str

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return self.value

class IntegerLiteral(Expression):
    def __init__(self, token, value):
        self.token = token     # token INT
        self.value = value     # int

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return str(self.value)

class PrefixExpression(Expression):
    def __init__(self, token, operator, right):
        self.token = token         # token '!' o '-'
        self.operator = operator   # str
        self.right = right         # Expression

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return f"({self.operator}{self.right})"

class InfixExpression(Expression):
    def __init__(self, token, left, operator, right):
        self.token = token         # el operador
        self.left = left           # Expression
        self.operator = operator   # str
        self.right = right         # Expression

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return f"({self.left} {self.operator} {self.right})"

class IfExpression(Expression):
    def __init__(self, token, condition, consequence, alternative):
        self.token = token
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        out = f"if {self.condition} {self.consequence}"
        if self.alternative:
            out += f" else {self.alternative}"
        return out

class BlockStatement(Statement):
    def __init__(self, token):
        self.token = token
        self.statements = []

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return "{ " + " ".join(str(stmt) for stmt in self.statements) + " }"
    
class WhileStatement(Statement):
    def __init__(self, token, condition, body):
        self.token = token        # token 'while'
        self.condition = condition
        self.body = body          # BlockStatement

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return f"while ({self.condition}) {self.body}"
class ForStatement(Statement):
    def __init__(self, token, init, condition, post, body):
        self.token = token          # 'for'
        self.init = init            # LetStatement or AssignStatement
        self.condition = condition  # Expression
        self.post = post            # Statement
        self.body = body            # BlockStatement

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return f"for ({self.init}; {self.condition}; {self.post}) {self.body}"
class AssignStatement(Statement):
    def __init__(self, token, name, value):
        self.token = token        # token '='
        self.name = name          # Identifier
        self.value = value        # Expression

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        return f"{self.name} = {self.value};"
class FunctionLiteral(Expression):
    def __init__(self, token, parameters, body):
        self.token = token            # token 'function'
        self.parameters = parameters  # lista de Identifiers
        self.body = body              # BlockStatement

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        params = ", ".join(str(p) for p in self.parameters)
        return f"{self.token_literal()}({params}) {self.body}"

class CallExpression(Expression):
    def __init__(self, token, function, arguments):
        self.token = token            # '(' token
        self.function = function      # Expression (puede ser Identifier o FunctionLiteral)
        self.arguments = arguments    # lista de Expressions

    def token_literal(self):
        return self.token.literal

    def __str__(self):
        args = ", ".join(str(a) for a in self.arguments)
        return f"{self.function}({args})"