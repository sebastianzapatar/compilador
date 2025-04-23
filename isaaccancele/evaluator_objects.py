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

# Constantes globales
TRUE = Boolean(True)
FALSE = Boolean(False)
