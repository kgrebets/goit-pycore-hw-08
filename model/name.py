from .field import Field

class Name(Field):
    def __init__(self, value):
        if not value:
            raise Exception("Name can't be empty")
        super().__init__(value)