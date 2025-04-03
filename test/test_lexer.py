from isaaccancele.lexer import Lexer
from isaaccancele.tokens import TokenType

def test_assing_token():
    lexer=Lexer("=")
    token=lexer.next_token()
    assert token.token_type==TokenType.ASSIGN

