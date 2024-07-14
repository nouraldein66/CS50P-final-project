class Player:
    def __init__(self, type, name, symbol):
        self._type = type
        self._name = name
        self._symbol = symbol

    @property
    def type(self):
        return self._type

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol