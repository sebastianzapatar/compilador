from enum import (
    auto,
    Enum,
    unique
)
from typing import NamedTuple

@unique
class TokenType(Enum):
    ASSIGN = auto()
    BANG = auto()
    COMMA = auto()
    EOF = auto()
    EQ = auto()
    NOT_EQ = auto()
    FOR = auto()
    FUNCTION = auto()
    IDENT = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    PLUS = auto()
    MINUS = auto()
    ASTERISK = auto()
    SLASH = auto()
    LT = auto()
    GT = auto()
    LE = auto()
    GE = auto()
    RBRACE = auto()
    RPAREN = auto()
    SEMICOLON = auto()

class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f"Token({self.token_type}, {self.literal})"

def lookup_token_type(literal: str) -> TokenType:
    keywords = {
        'function': TokenType.FUNCTION,
        'let': TokenType.LET,
        'for': TokenType.FOR
    }
    return keywords.get(literal, TokenType.IDENT)
