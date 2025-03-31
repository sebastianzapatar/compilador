from re import match
from isaaccancele.tokens import (
    Token,
    TokenType
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
        
        if match(r"^=$", self.character):
            token = Token(TokenType.ASSIGN, self.character)
        elif match(r"^\+$", self.character):
            token = Token(TokenType.PLUS, self.character)
        elif self.character == '':  # Manejo correcto del EOF
            return Token(TokenType.EOF, "")
        else:
            token = Token(TokenType.ILLEGAL, self.character)

        self.read_char()  # ¡Esto es clave para evitar el ciclo infinito!
        return token

    def skip_whitespace(self) -> None:
        while match(r"^\s$", self.character):
            self.read_char()

    def read_char(self) -> None:
        if self.read_position >= len(self.source):
            self.character = ''
        else:
            self.character = self.source[self.read_position]

        self.position = self.read_position
        self.read_position += 1
