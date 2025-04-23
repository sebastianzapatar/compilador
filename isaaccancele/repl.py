from isaaccancele.lexer import Lexer
from isaaccancele.parser import Parser
from isaaccancele.evaluator import eval_node
from isaaccancele.evaluator import environment

def start_repl():
    print("Welcome to Isaac Cancele's Monkey REPL")
    print("Type 'exit' to exit")

    while True:
        try:
            source = input(">> ")
            if source.strip().lower() == "exit":
                break

            lexer = Lexer(source)
            parser = Parser(lexer)
            program = parser.parse_program()

            # Mostrar errores de parsing si los hay
            if parser.errors:
                print("Parser errors:")
                for err in parser.errors:
                    print(f"  ✖ {err}")
                continue  # No evalúes si hay errores

            # Opcional: imprimir el AST parseado
            # print("AST:")
            # print(program)

            result = eval_node(program)
            if result is not None:
                print(result.inspect())

        except Exception as e:
            print(f"Runtime Error: {e}")
