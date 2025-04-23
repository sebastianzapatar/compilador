
from isaaccancele.lexer import Lexer
from isaaccancele.parser import Parser
from isaaccancele.evaluator import eval_node

# Entorno persistente entre múltiples entradas del usuario
from isaaccancele.evaluator import environment

def start_repl():
    print("Welcome to Isaac Cancele's Monkey REPL")
    print("Type 'exit' to exit")

    while True:
        try:
            source = input(">> ")
            if source.strip() == "exit":
                break

            lexer = Lexer(source)
            parser = Parser(lexer)
            program = parser.parse_program()

            result = eval_node(program)
            if result is not None:
                print(result.inspect())
        except Exception as e:
            print(f"Error: {e}")
