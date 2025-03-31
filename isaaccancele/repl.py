# isaaccancele/repl.py

from isaaccancele.lexer import Lexer
from isaaccancele.parser import Parser
from isaaccancele.ast import Program

def start_repl():
    while (source := input(">> ")) != "exit":
        lexer = Lexer(source)
        parser = Parser(lexer)
        program: Program = parser.parse_program()

        for stmt in program.statements:
            print(stmt.token_literal(), stmt.__class__.__name__)
