# environment.py

class Environment:
    def __init__(self, outer=None):
        self.store = {}
        self.outer = outer  # Entorno padre (puede ser None)

    def get(self, name):
        value = self.store.get(name)
        if value is None and self.outer is not None:
            return self.outer.get(name)
        return value

    def set(self, name, value):
        self.store[name] = value
