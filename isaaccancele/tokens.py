from enum import(
    auto,
    Enum,
    unique
)
from typing import NamedTuple

@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    EOF=auto()
    EQ=auto()
    FOR=auto()
    FUNCTION=auto()
    IDENT=auto()
    ILLEGAL=auto()
    INT=auto()
    LBRACE=auto()
    LET=auto()
    LPAREN=auto()
    PLUS=auto()
    RBRACE=auto()
    RPAREN=auto()
    SEMICOLON=auto()

class Token(NamedTuple):
    token_type: TokenType
    literal: str
    def __str__(self)->str:
        return f"Token({self.token_type}, {self.literal})"
def lookup_token_type(literal:str)->TokenType:
    keyword={'function':TokenType.FUNCTION,
             'let':TokenType.LET,
             'for':TokenType.FOR
            }
    return keyword.get(literal,TokenType.IDENT)
        
