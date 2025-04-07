from isaaccancele.lexer import Lexer
from isaaccancele.parser import Parser
from isaaccancele.evaluator import eval_node

def start_repl():
    while (source := input(">> ")) != "exit":
        lexer = Lexer(source)
        parser = Parser(lexer)
        program = parser.parse_program()

        result = eval_node(program)
        if result:
            print(result.inspect())
"""
from isaaccancele.lexer import Lexer
from isaaccancele.parser import Parser

while True:
    source = input(">> ")
    if source == "exit":
        break
    lexer = Lexer(source)
    parser = Parser(lexer)
    program = parser.parse_program()
    print(program)

"""