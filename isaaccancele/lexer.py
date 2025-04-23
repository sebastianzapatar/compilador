from re import match
from isaaccancele.tokens import (
    Token,
    TokenType,
    lookup_token_type
)

class Lexer:
    def __init__(self, source):
        self.source = source
        self.character = ''
        self.read_position = 0
        self.position = 0
        self.read_char()

    def next_token(self) -> Token:
        self.skip_whitespace()

        if self.character == '=':
            if self._peek_character() == '=':
                self.read_char()
                token = Token(TokenType.EQ, "==")
            else:
                token = Token(TokenType.ASSIGN, self.character)
        elif self.character == '!':
            if self._peek_character() == '=':
                self.read_char()
                token = Token(TokenType.NOT_EQ, "!=")
            else:
                token = Token(TokenType.BANG, "!")
        elif self.character == '+':
            token = Token(TokenType.PLUS, self.character)
        elif self.character == '-':
            token = Token(TokenType.MINUS, self.character)
        elif self.character == '*':
            token = Token(TokenType.ASTERISK, self.character)
        elif self.character == '/':
            token = Token(TokenType.SLASH, self.character)
        elif self.character == '<':
            if self._peek_character() == '=':
                self.read_char()
                token = Token(TokenType.LE, "<=")
            else:
                token = Token(TokenType.LT, self.character)
        elif self.character == '>':
            if self._peek_character() == '=':
                self.read_char()
                token = Token(TokenType.GE, ">=")
            else:
                token = Token(TokenType.GT, self.character)
        elif self.character == '(':
            token = Token(TokenType.LPAREN, self.character)
        elif self.character == ')':
            token = Token(TokenType.RPAREN, self.character)
        elif self.character == '{':
            token = Token(TokenType.LBRACE, self.character)
        elif self.character == '}':
            token = Token(TokenType.RBRACE, self.character)
        elif self.character == ',':
            token = Token(TokenType.COMMA, self.character)
        elif self.character == ';':
            token = Token(TokenType.SEMICOLON, self.character)
        elif self._is_number(self.character):
            number = self._read_number()
            return Token(TokenType.INT, number)
        elif self._is_letter(self.character):
            literal = self._read_literal()
            token_type = lookup_token_type(literal)
            return Token(token_type, literal)
        elif self.character == '':
            return Token(TokenType.EOF, "")
        else:
            token = Token(TokenType.ILLEGAL, self.character)

        self.read_char()
        return token

    def skip_whitespace(self) -> None:
        while match(r"^\s$", self.character):
            self.read_char()

    def _is_number(self, character: str) -> bool:
        return bool(match(r'^\d$', character))

    def _is_letter(self, character: str) -> bool:
        return bool(match(r'^[a-zA-Z]$', character))

    def _read_number(self) -> str:
        initial_position = self.position
        while self._is_number(self.character):
            self.read_char()
        return self.source[initial_position:self.position]

    def _read_literal(self) -> str:
        initial_position = self.position
        while self._is_letter(self.character) or self._is_number(self.character):
            self.read_char()
        return self.source[initial_position:self.position]

    def read_char(self) -> None:
        if self.read_position >= len(self.source):
            self.character = ''
        else:
            self.character = self.source[self.read_position]

        self.position = self.read_position
        self.read_position += 1

    def _peek_character(self) -> str:
        if self.read_position >= len(self.source):
            return ''
        return self.source[self.read_position]
