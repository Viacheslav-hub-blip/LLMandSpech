class SomeClass():
    def __init__(self, value):
        self._value = value

    def __getattr__(self, value):
        return self._value

    def __setattr__(self,  key, value):
        self._value = value

    def delvalue(self):
        del self._value
