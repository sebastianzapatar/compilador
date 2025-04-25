# evaluator_objects.py

class Object:
    def type(self):
        raise NotImplementedError()

    def inspect(self):
        raise NotImplementedError()

class Integer(Object):
    def __init__(self, value: int):
        self.value = value

    def type(self):
        return "INTEGER"

    def inspect(self):
        return str(self.value)

class Boolean(Object):
    def __init__(self, value: bool):
        self.value = value

    def type(self):
        return "BOOLEAN"

    def inspect(self):
        return "true" if self.value else "false"
class Function(Object):
    def __init__(self, parameters, body, env):
        self.parameters = parameters  # lista de Identifiers
        self.body = body              # BlockStatement
        self.env = env                # entorno donde fue definida

    def type(self):
        return "FUNCTION"

    def inspect(self):
        params = ", ".join(str(p) for p in self.parameters)
        return f"function({params}) {{ {str(self.body)} }}"

# Constantes globales
TRUE = Boolean(True)
FALSE = Boolean(False)
