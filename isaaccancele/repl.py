from isaaccancele.lexer import Lexer
from isaaccancele.tokens import (
    Token,
    TokenType
)
EOF_TOKEN=Token(TokenType.EOF, '')

def start_repl():
    while (source:=input(">> "))!="exit":
        lexer=Lexer(source)

        while (token:=lexer.next_token())!=EOF_TOKEN:
            print(token)