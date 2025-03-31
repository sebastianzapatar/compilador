# tests/test_parser.py

from isaaccancele.lexer import Lexer
from isaaccancele.parser import Parser
from isaaccancele.ast import LetStatement, Identifier

def test_parse_let_statement():
    input_code = "let myVar = anotherVar;"

    lexer = Lexer(input_code)
    parser = Parser(lexer)
    program = parser.parse_program()

    # Asegurarse de que haya una única declaración
    assert len(program.statements) == 1

    stmt = program.statements[0]

    # Verificamos que sea un LetStatement
    assert isinstance(stmt, LetStatement)
    assert stmt.token_literal() == "let"

    # Verificamos que el nombre del identificador sea correcto
    assert isinstance(stmt.name, Identifier)
    assert stmt.name.value == "myVar"
    assert stmt.name.token_literal() == "myVar"
