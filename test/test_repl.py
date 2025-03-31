from unittest.mock import patch
from isaaccancele.repl import start_repl

def test_repl_prints_tokens(capsys):
    with patch("builtins.input", side_effect=["=", "exit"]):
        start_repl()
    captured = capsys.readouterr()
    assert "Token(TokenType.ASSIGN, =)" in captured.out
