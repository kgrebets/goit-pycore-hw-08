from load_save_data import load_data, save_data
from model.addressBook import AddressBook
from model.record import Record
from command_check_decorator import command_check_decorator
from parse_input_validator import parse_input_validator

@parse_input_validator
def parse_input(cmd_string):
    cmd, *args = cmd_string.split()
    cmd = cmd.strip().lower()
    return (cmd, args)


@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: add [name] [phone number]"
        ) 
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: change [name] [old phone] [new phone number]"
        ) 
def change_contact(args, book:AddressBook):
    name, old_phone, new_phone = args
    if name in book:
        r = book[name]
        r.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        raise Exception("Error: Contact not found.")


@command_check_decorator(
        index_error_message="Error: Not enough arguments. Usage: delete [name]",
        key_error_message= "Error: Contact not found"
        ) 
def delete_contact(args, book:AddressBook):
    name = args[0]
    book.pop(name)
    return "Contact removed."


@command_check_decorator(
        index_error_message="Error: Not enough arguments. Usage: phone [name]",
        key_error_message= "Error: Contact not found"
        )
def show_phone(args, book:AddressBook):
    name = args[0]
    contact_strings = [p.value for p in book[name].phones]
    result = ", ".join(contact_strings)
    return result


def show_all(book:AddressBook):
    if len(book) == 0:
        return "No contacts found."

    contact_strings = [str(record) for _, record in book.data.items()]
    result = "\n".join(contact_strings)
    return result


@command_check_decorator(
        value_error_message="Error: Not enough arguments. Usage: add-birthday [name] [birthday (DD.MM.YYYY)]"
        ) 
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    record.add_birthday(birthday)
    return "Contact updated"


@command_check_decorator()
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record is None:
        raise Exception(f"No '{name}' contact found")
    return record.birthday.value.strftime("%d.%m.%Y")


def show_upcoming_birthdays(book: AddressBook):
    items = book.get_upcoming_birthdays()
    birthday_strings = [f"{x['name']} - {x['congratulation_date']}" for x in items]
    result = "\n".join(birthday_strings)
    return result


def main():
    book = AddressBook()
    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        cmd_string = input("Enter a command: ")
        cmd, args = parse_input(cmd_string)
                
        if cmd in ["close", "exit"]:
            print("Good bye!")
            break

        elif cmd == "hello":
            print("How can I help you?")

        elif cmd == "add":
            print(add_contact(args, book))

        elif cmd == "change":
            print(change_contact(args, book))

        elif cmd == "delete":
            print(delete_contact(args, book))

        elif cmd == "phone":
            print(show_phone(args, book))

        elif cmd == "all":
            print(show_all(book))
            
        elif cmd == "add-birthday":
            print(add_birthday(args, book))

        elif cmd == "show-birthday":
            print(show_birthday(args, book))

        elif cmd == "birthdays":
            print(show_upcoming_birthdays(book))

        else:
            print("Invalid command.")
    save_data(book) 
main()