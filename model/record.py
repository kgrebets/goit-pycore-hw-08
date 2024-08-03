from .name import Name
from .phone import Phone
from .birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        phones = '; '.join(ph.value for ph in self.phones)
        birthday_str = self.birthday.value.strftime('%d.%m.%Y') if self.birthday else 'N/A'
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday_str}"
    
    def add_phone(self, phone:str):
        for ph in self.phones:
            if(ph.value == phone):
                return
        self.phones.append(Phone(phone))

    def remove_phone(self, phone:str):
        ph = self.find_phone(phone) 
        index_to_delete = self.phones.index(ph) 
        self.phones.pop(index_to_delete)

    def edit_phone(self, old_phone:str, new_phone:str):
        for ind, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[ind] = Phone(new_phone)
                return
        raise Exception(f"No {old_phone} phone found for {self.name.value}")
    
    def find_phone(self, phone:str):
        for  ph in self.phones:
            if phone == ph.value:
                return ph
        raise Exception(f"No {ph} phone found for {self.name.value}")
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
 