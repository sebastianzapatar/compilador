# Crear el README en formato Markdown bonito
readme_content = """
# 🐒 Intérprete Monkey - Instrucciones de Uso

---

# 🔄 Descripción General

Este proyecto implementa un **intérprete** de un lenguaje estilo Monkey.
Permite evaluar:
- Operaciones matemáticas.
- Asignaciones de variables.
- Condicionales (`if` / `else`).
- Bucles (`while`, `for`).
- **Funciones** con parámetros, llamadas y recursividad.

---

# 📁 Estructura del Proyecto


- **`isaaccancele/`** contiene el código del intérprete.
- **`main.py`** es el archivo principal que lee archivos `.monkey`.
- **`ejemplos/`** carpeta sugerida para guardar tus programas Monkey.

---

# 📅 Requisitos

- Python 3.8 o superior instalado.

No se requieren librerías externas.

---

# 🔍 ¿Cómo ejecutar el intérprete?

1. **Coloca tu archivo `.monkey`** en alguna ruta. Ejemplo: `ejemplos/prueba.monkey`

2. **Estructura de tu `main.py`** (ejemplo sugerido):

```python
from isaaccancele.lexer import Lexer
from isaaccancele.parser import Parser
from isaaccancele.evaluator import eval_node, global_env

if __name__ == "__main__":
    with open("ejemplos/prueba.monkey", "r") as f:
        source = f.read()

    lexer = Lexer(source)
    parser = Parser(lexer)
    program = parser.parse_program()

    if parser.errors:
        print("Errores de parseo:")
        for err in parser.errors:
            print(f"  ✖ {err}")
    else:
        eval_node(program)
python main.py

let factorial = function(n) {
  if (n == 0) {
    1;
  } else {
    n * factorial(n - 1);
  }
};

let resultado = factorial(5);
resultado;


