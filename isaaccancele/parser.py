from isaaccancele.tokens import TokenType, Token
from isaaccancele.ast import *
from isaaccancele.lexer import Lexer

PRECEDENCES = {
    TokenType.EQ: 2,
    TokenType.NOT_EQ: 2,
    TokenType.LT: 2,
    TokenType.GT: 2,
    TokenType.LE: 2,
    TokenType.GE: 2,
    TokenType.PLUS: 3,
    TokenType.MINUS: 3,
    TokenType.SLASH: 4,
    TokenType.ASTERISK: 4,
}

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = None
        self.peek_token = None
        self.errors = []

        self._advance()
        self._advance()

    def _advance(self):
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self):
        program = Program()
        while self.current_token.token_type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                program.statements.append(stmt)
            self._advance()
        return program

    
    def parse_statement(self):
        if self.current_token.token_type == TokenType.LET:
            return self._parse_let_statement()
        return self.parse_expression_statement()

    def _parse_let_statement(self):
        token = self.current_token  # 'let'

        if not self._expect_peek(TokenType.IDENT):
            return None
        name = Identifier(self.current_token, self.current_token.literal)

        if not self._expect_peek(TokenType.ASSIGN):
            return None
        self._advance()  # skip '='

        value = self.parse_expression(0)

        if self.peek_token.token_type == TokenType.SEMICOLON:
            self._advance()

        return LetStatement(token, name, value)

    def _expect_peek(self, ttype):
        if self.peek_token.token_type == ttype:
            self._advance()
            return True
        self.errors.append(f"Expected next token to be {ttype}, got {self.peek_token.token_type} instead.")
        return False


    def parse_expression_statement(self):
        expr = self.parse_expression(0)
        return ExpressionStatement(self.current_token, expr)

    def parse_expression(self, precedence):
        prefix_fn = self._prefix_parse_fns().get(self.current_token.token_type)
        if not prefix_fn:
            self.errors.append(f"No prefix parse function for {self.current_token.token_type}")
            return None
        left_expr = prefix_fn()

        while (self.peek_token.token_type != TokenType.SEMICOLON and
               precedence < self._peek_precedence()):
            infix_fn = self._infix_parse_fns().get(self.peek_token.token_type)
            if not infix_fn:
                return left_expr
            self._advance()
            left_expr = infix_fn(left_expr)
        return left_expr

    def _prefix_parse_fns(self):
        return {
            TokenType.IDENT: self._parse_identifier,
            TokenType.INT: self._parse_integer_literal,
            TokenType.BANG: self._parse_prefix_expression,
            TokenType.MINUS: self._parse_prefix_expression,
            TokenType.IF: self._parse_if_expression,
        }

    def _infix_parse_fns(self):
        return {
            TokenType.PLUS: self._parse_infix_expression,
            TokenType.MINUS: self._parse_infix_expression,
            TokenType.SLASH: self._parse_infix_expression,
            TokenType.ASTERISK: self._parse_infix_expression,
            TokenType.EQ: self._parse_infix_expression,
            TokenType.NOT_EQ: self._parse_infix_expression,
            TokenType.LT: self._parse_infix_expression,
            TokenType.GT: self._parse_infix_expression,
            TokenType.LE: self._parse_infix_expression,
            TokenType.GE: self._parse_infix_expression,
        }

    def _parse_identifier(self):
        return Identifier(self.current_token, self.current_token.literal)

    def _parse_integer_literal(self):
        try:
            value = int(self.current_token.literal)
        except ValueError:
            self.errors.append(f"Could not parse {self.current_token.literal} as integer.")
            return None
        return IntegerLiteral(self.current_token, value)

    def _parse_prefix_expression(self):
        token = self.current_token
        operator = token.literal
        self._advance()
        right = self.parse_expression(5)
        return PrefixExpression(token, operator, right)

    def _parse_infix_expression(self, left):
        token = self.current_token
        operator = token.literal
        precedence = self._current_precedence()
        self._advance()
        right = self.parse_expression(precedence)
        return InfixExpression(token, left, operator, right)

    def _peek_precedence(self):
        return PRECEDENCES.get(self.peek_token.token_type, 0)

    def _current_precedence(self):
        return PRECEDENCES.get(self.current_token.token_type, 0)



    def _parse_if_expression(self):
        token = self.current_token  # token 'if'

        if not self._expect_peek(TokenType.LPAREN):
            return None
        self._advance()
        condition = self.parse_expression(0)
        if not self._expect_peek(TokenType.RPAREN):
            return None

        if not self._expect_peek(TokenType.LBRACE):
            return None
        consequence = self._parse_block_statement()

        alternative = None
        if self.peek_token.token_type == TokenType.ELSE:
            self._advance()
            if self.peek_token.token_type == TokenType.IF:
                self._advance()
                alternative = self._parse_if_expression()
            elif self._expect_peek(TokenType.LBRACE):
                alternative = self._parse_block_statement()

        return IfExpression(token, condition, consequence, alternative)


    def _parse_block_statement(self):
        token = self.current_token
        block = BlockStatement(token)
        self._advance()

        while self.current_token.token_type != TokenType.RBRACE and self.current_token.token_type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                block.statements.append(stmt)
            self._advance()

        return block
