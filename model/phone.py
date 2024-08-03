import re
from .field import Field

class Phone(Field):
    def __init__(self, value):
        if not re.match(r'^\d{10}$', value):
            raise Exception("Phone number must be 10 digits long")
        super().__init__(value)