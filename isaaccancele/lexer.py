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
        
        if match(r"^=$", self.character):
            if self._peek_character()=='=':
                token=Token(TokenType.EQ,"==")
                self.read_char()
            else:
                token = Token(TokenType.ASSIGN, self.character)
        elif match(r"^\+$", self.character):
            token = Token(TokenType.PLUS, self.character)
        elif self._is_number(self.character):
            number=self._read_number()
            tokenType=TokenType.INT
            return Token(tokenType,number)
        elif self._is_letter(self.character):
            literal=self._read_literal()
            tokenType=lookup_token_type(literal)
            return Token(tokenType,literal)
        elif self.character == '':  # Manejo correcto del EOF
            return Token(TokenType.EOF, "")
        else:
            token = Token(TokenType.ILLEGAL, self.character)

        self.read_char()  # ¡Esto es clave para evitar el ciclo infinito!
        return token
    def skip_whitespace(self) -> None:
        while match(r"^\s$", self.character):
            self.read_char()
    def _is_number(self,character:str)->bool:
        return bool(match(r'^\d$',character))
    def _is_letter(self,character):
        return bool(match(r'^[a-zA-Z]',character))
    def _read_number(self)->str:
        initial_position=self.position
        while self._is_number(self.character):
            self.read_char()
        return self.source[initial_position:self.position]
    def _read_literal(self):
        initial_position=self.position
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
    def _peek_character(self):
        if self.read_position>=len(self.source):
            return ''
        return self.source[self.read_position]