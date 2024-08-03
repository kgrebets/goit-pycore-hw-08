from datetime import datetime
from .field import Field

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, '%d.%m.%Y').date()
        except Exception:
            raise Exception("Invalid date format. Use DD.MM.YYYY")