
from classField import Field
from classBirthday import Birthday
from classMail import Email
from classPhone import Phone
from classContact import Name
from collections import UserDict


# entry in a contact
class Record(Field):

    # Creates objects for name, birthday, and email using
    def __init__(self, name, birthday=None, email=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None
        self.email = Email(email) if email else None

# This casts the value of the value attribute to a string and returns it
    def __str__(self):
        return f"Contact name: {self.name.value}, \
phones: {'; '.join(p.value for p in self.phones)}" \
               f", birthday: {self.birthday.value}, {self.email}" \
                if self.birthday else ""

# Adds a new phone number to the contact's phone list, if such a number does
# not already exist.
    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if not any(existing_phone.value == phone.value for
                   existing_phone in self.phones):
            self.phones.append(phone)

# Searches for a phone number in the contact's phone list and returns a
# matching Phone object if found.
    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

# Replaces the old phone number with the new one in the contact's phone list
# if the old number is found and the new number matches the validation rules.
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                try:
                    phone.validate(new_phone)
                    phone.value = new_phone
                    return new_phone
                except ValueError as e:
                    print(e)
        raise ValueError(f"Phone number {old_phone} not found.")

# Removes a phone number from the contact's phone list, if such a
# number exists.
    def delete_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return phone.value
        raise ValueError(f"Phone number {phone_number} not found.")

# Calculates the number of days until the next birthday if the contact's
# birthday is specified
    def days_to_birthday(self):
        if self.birthday:
            return self.birthday.days_until_next_birthday()
        return None


class ContactBook(UserDict):

    # add and save new record of contact into the book
    def add_record(self, record: Record):
        self.data[record.name.value] = record

# find record of contact in book
    def find(self, name):
        return self.data.get(name)

# delete record of contact from the book
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"The contact {name} deleted.")
        else:
            print(f"The contact {name} not found.")

# add new record of contact into the book
    def add(self, name, address):
        self.data[name] = address

# forms a result string that contains information about each record as a string
    def iterator(self, item_number):
        counter = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {record}\n'
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ''

    def edit(self, name, new_record: Record):
        if name in self.data:
            self.data[name] = new_record
            print(f"The contact {name} has been edited.")
        else:
            print(f"The contact {name} not found.")


address_book = ContactBook()

# # Створення контакту
# record1 = Record(name="John Doe", birthday="01.01.1990",
#                  email="john@example.com")
# record2 = Record(name="Jane Doe", birthday="05.05.1995",
#                  email="jane@example.com")
# print(record1)
# print(record2)
# # Додавання контактів до адресної книги
# address_book.add_record(record1)
# address_book.add_record(record2)

# # Виведення всіх контактів
# print("All contacts:")
# for item, record in address_book.data.items():
#     print(f'{item}: {record}')

# # Редагування контакту
# edited_record = Record(name="John Doe", birthday="01.01.1990",
#                        email="john.doe@example.com")
# address_book.edit("John Doe", edited_record)

# # Виведення всіх контактів після редагування
# print("\nAll contacts after editing:")
# for item, record in address_book.data.items():
#     print(f'{item}: {record}')
