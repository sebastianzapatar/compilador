
from isaaccancele.lexer import Lexer
from isaaccancele.parser import Parser
from isaaccancele.evaluator import eval_node, environment

def run_file(filename):
    try:
        with open(filename, 'r') as file:
            source = file.read()

            lexer = Lexer(source)
            parser = Parser(lexer)
            program = parser.parse_program()

            if parser.errors:
                for error in parser.errors:
                    print(f"Parser error: {error}")
                return

            eval_node(program)  # Ahora imprime todo internamente
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filename}")
    except Exception as e:
        print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    run_file("compilador.monkey")
