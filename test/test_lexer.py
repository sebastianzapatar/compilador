from isaaccancele.lexer import Lexer
from isaaccancele.tokens import TokenType
def test_assign_token():
    

    lexer = Lexer("=")
    token = lexer.next_token()
    assert token.token_type == TokenType.ASSIGN
    assert token.literal == "="

def test_assign_token():
    

    lexer = Lexer("=")
    token = lexer.next_token()
    assert token.token_type == TokenType.ASSIGN
    assert token.literal == "="

def test_plus_token():
    lexer = Lexer("+")
    token = lexer.next_token()
    assert token.token_type == TokenType.PLUS
    assert token.literal == "+"

def test_illegal_token():
    lexer = Lexer("?")
    token = lexer.next_token()
    assert token.token_type == TokenType.ILLEGAL
    assert token.literal == "?"

def test_skip_whitespace():
    lexer = Lexer("     +")
    token = lexer.next_token()
    assert token.token_type == TokenType.PLUS
