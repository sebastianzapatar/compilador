# isaaccancele/parser.py
from isaaccancele.lexer import Lexer
from isaaccancele.tokens import Token, TokenType
from isaaccancele.ast import Program, LetStatement, Identifier

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token: Token = None
        self.peek_token: Token = None
        self.next_token()
        self.next_token()

    def next_token(self):
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self) -> Program:
        program = Program()
        while self.current_token.token_type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                program.statements.append(stmt)
            self.next_token()
        return program

    def parse_statement(self):
        if self.current_token.token_type == TokenType.LET:
            return self.parse_let_statement()
        return None

    def parse_let_statement(self):
        token = self.current_token  # 'let'
        if not self.expect_peek(TokenType.IDENT):
            return None

        name = Identifier(self.current_token, self.current_token.literal)

        if not self.expect_peek(TokenType.ASSIGN):
            return None

        # TODO: parse expression for now, skipping until semicolon
        while self.current_token.token_type != TokenType.SEMICOLON:
            self.next_token()

        return LetStatement(token, name, None)

    def expect_peek(self, t: TokenType) -> bool:
        if self.peek_token.token_type == t:
            self.next_token()
            return True
        return False
