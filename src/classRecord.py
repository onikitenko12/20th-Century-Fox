from classField import Field
from classBirthday import Birthday
from classMail import Email
from classPhone import Phone
from classContact import Name
from collections import UserDict
from classAddress import Address
from datetime import datetime
import json


class DataManager:
    def __init__(self, filename="contacts_data.json"):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([record.to_dict() for record in data.values()], file, ensure_ascii=False)

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []


# entry in a contact
class Record(Field):
    phone_index = {}

    # Creates objects for name, birthday, and email using
    def __init__(self, name, birthday=None, email=None, address=None, phones=None):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones] if phones else []
        self.birthday = Birthday(birthday) if birthday else None
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None

    def to_dict(self):
        return {
            "name": self.name.value,
            "phones": [phone.value for phone in self.phones],
            "birthday": self.birthday.value.strftime("%d.%m.%Y") if self.birthday else None,
            "email": self.email.value if self.email else None,
            "address": self.address.value if self.address else None
        }

# This casts the value of the value attribute to a string and returns it
    def __str__(self):
        result = f"Contact name: {self.name.value}, " \
            f"phones: {'; '.join(p.value for p in self.phones)}, " \
            f"birthday: {self.birthday.value if self.birthday else 'Not specified'}, " \
            f"email: {self.email.value if self.email else 'Not specified'}, " \
            f"address: {self.address.value if self.address else 'Not specified'}, "
        return result

    def has_phone(self, phone_number):
        return any(phone.value == phone_number for phone in self.phones)

# Adds a new phone number to the contact's phone list, if such a number does
# not already exist.
    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if not any(existing_phone.value == phone.value for existing_phone in self.phones):
            self.phones.append(phone)
            if phone.value not in Record.phone_index:
                Record.phone_index[phone.value] = [self.name.value]
            else:
                Record.phone_index[phone.value].append(self.name.value)

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
                    if old_phone in Record.phone_index:
                        Record.phone_index[new_phone] = Record.phone_index.pop(old_phone)
                    phone.value = new_phone
                    return new_phone
                except ValueError as e:
                    print(e)
        raise ValueError(f"Phone number {old_phone} not found.")

    def edit_phone_number(self, old_phone, new_phone):
        try:
            self.edit_phone(old_phone, new_phone)
            print(f"Phone number for {self.name.value} has been updated.")
        except ValueError as e:
            print(e)

    def edit_address(self, new_address):
        if self.address:
            self.address.value = new_address
            print(f"Address for {self.name.value} has been updated.")
        else:
            print(f"{self.name.value} does not have an existing address. Use set_address to add one.")

    def edit_birthday(self, new_birthday):
        if new_birthday:
            try:
                self.birthday = Birthday(new_birthday)
                print(f"Birthday for {self.name.value} has been updated.")
            except ValueError as e:
                print(e)
        else:
            print("Invalid birthday value.")

# Removes a phone number from the contact's phone list, if such a
# number exists.
    def delete_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return phone.value
        raise ValueError(f"Phone number {phone_number} not found.")

    def delete_birthday(self):
        self.birthday = None

    def delete_email(self):
        if self.email:
            deleted_email = self.email.value
            self.email = None
            return deleted_email
        return None

    def set_address(self, address):
        if not self.address:
            self.address = Address(address)
        else:
            self.address.value = address

    def set_birthday(self, birthday):
        self.birthday = Birthday(birthday)

# Calculates the number of days until the next birthday if the contact's
# birthday is specified
    def days_to_birthday(self):
        if self.birthday:
            return self.birthday.days_until_next_birthday()
        return None


class ContactBook(UserDict):
    def __init__(self, data_manager=None):
        super().__init__()
        self.phone_index = {}
        self.data_manager = data_manager or DataManager()
        self.load_data()
        self.build_phone_index()

# add and save new record of contact into the book
    def add_record(self, record: Record):
        self.__setitem__(record.name.value, record)
        self.data_manager.save_data(self.data)

# find record of contact in book
    def find(self, name):
        return self.data.get(name)

# delete record of contact from the book
    def delete(self, name):
        super().__delitem__(name)
        self.data_manager.save_data(self.data)

# add new record of contact into the book
    def add_phone_to_contact(self, name, phone_number):
        if name in self.data:
            contact = self.data[name]
            contact.add_phone(phone_number)
            self.data_manager.save_data(self.data)

# forms a result string that contains information about each record as a string
    def iterator(self, item_number):
        counter = 0
        result = ''
        for record in self.data.values():
            result += f'{record}, Days to Birthday: {record.days_to_birthday()}\n'
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ''

    def find_by_phone(self, phone_number):
        names = self.phone_index.get(phone_number, [])
        if isinstance(names, list):
            contacts = [self.data[name] for name in names if name in self.data]
            return contacts
        elif isinstance(names, str) and names in self.data:
            return [self.data[names]]
        else:
            return []

    def find_by_name(self, name):
        name = Name(name)
        for record in self.data.values():
            if record.name.value == name.value:
                return record
        return None

    def find_by_email(self, email):
        result = []
        for record in self.data.values():
            if record.email and record.email.value == email:
                result.append(record)
        return result

    def find_by_address(self, address):
        matching_contacts = []
        for record in self.data.values():
            if record.address and record.address.value == address:
                matching_contacts.append(record)
        return matching_contacts

    def find_by_birthday(self, birthday):
        matching_contacts = []
        for record in self.data.values():
            if record.birthday and record.birthday.value == birthday:
                matching_contacts.append(record)
        return matching_contacts

    def load_data(self):
        loaded_data = self.data_manager.load_data()
        for record_data in loaded_data:
            name, record = record_data["name"], record_data
            self.data[name] = Record(**record)

    def edit(self, name, new_record: Record):
        old_record = self.data[name]
        for phone in old_record.phones:
            if phone.value in self.phone_index and name in self.phone_index[phone.value]:
                self.phone_index[phone.value].remove(name)
                if not self.phone_index[phone.value]:
                    del self.phone_index[phone.value]
        self.__setitem__(name, new_record)
        self.update_phone_index(new_record)
        self.data_manager.save_data(self.data)

    def update_phone_index(self, record: Record):
        for phone in record.phones:
            if phone.value not in self.phone_index:
                self.phone_index[phone.value] = [record.name.value]
            else:
                if record.name.value not in self.phone_index[phone.value]:
                    self.phone_index[phone.value].append(record.name.value)

    def build_phone_index(self):
        self.phone_index = {}
        for name, record in self.data.items():
            for phone in record.phones:
                if phone.value not in self.phone_index:
                    self.phone_index[phone.value] = [name]
                else:
                    self.phone_index[phone.value].append(name)


# Create object Address Book
address_book = ContactBook(data_manager=DataManager())

# Create object DataManager
data_manager = DataManager()

# Create object ContactBook with giving data_manager
address_book = ContactBook(data_manager=data_manager)

# # Create contact for adding to Address Book
# user = Record(name="user_name", birthday="15.12.2000", email="user_email@.com")
# # record2 = Record(name="Jane Doe", birthday="05.05.1995", email="jane@example.com")
# # record3 = Record(name="Anna Barbach", email="Anna555@example.com")

# user.add_phone("9523380090")
# # record2.add_phone("9876533321")
# # record3.add_phone("9876511121")

# address_book.add_record(user)
# # address_book.add_record(record2)
# # address_book.add_record(record3)
# # Виведення всіх контактів з адресної книги
# print("All contacts in the address book:")
# for contact_info in address_book.iterator(item_number=len(address_book)):
#     print(contact_info)


# # Add address to contacts
# # Search contact by name (example, "John Doe")
# # contact_to_edit = address_book.find("Nick CouK")

# if address_book.find("Nick CouK"):
#     # Add address to contacts
#     address_book.find("Nick CouK").set_address("15-02 LiveRpul O'Hara Street")

#     # Save changes
#     address_book.edit("Nick CouK", address_book.find("Nick CouK"))

#     # Show all contacts after editing and updating
#     print("\nAll contacts after editing and updating:")
#     for contact_info in address_book.iterator(item_number=len(address_book)):
#         print(contact_info)

#     print("Address added successfully.")
# else:
#     print("Contact not found.")


# # Add Birthday to contact
# # Search contact by name (Exsample, "Anna Barbach")
# contact_to_edit = address_book.find("user_name")

# if contact_to_edit:
#     # Add Birthday to contact
#     contact_to_edit.set_birthday("user_date")

#     # Save changes
#     address_book.edit("user_name", contact_to_edit)

#     # Show all contacts after editing and updating
# #     print("\nAll contacts after editing and updating:")
# #     for contact_info in address_book.iterator(item_number=len(address_book)):
# #         print(contact_info)

# #     print("Birthday added successfully.")
# # else:
# #     print("Contact not found.")


# # Search contact by name
# # name_to_find = "John Doe"
# found_contact = address_book.find_by_name("user_name")

# # if found_contact:
# #     print(f"\nContacts with name {name_to_find} found:")
# #     print(found_contact)
# # else:
# #     print(f"\nContacts with name {name_to_find} not found")


# # Search contact by phone number
# # phone_number_to_find = "9995588443"
# found_contacts = address_book.find_by_phone(user_number)

# # if found_contacts:
# #     print(f"\nContacts with phone number {phone_number_to_find} found:")
# #     for contact in found_contacts:
# #         print(contact)
# # else:
# #     print(f"\nNo contacts found with phone number {phone_number_to_find}")


# # Search contact by email
# # email_to_find = "Anna555@example.com"
# found_contacts_by_email = address_book.find_by_email(user_email)

# # if found_contacts_by_email:
# #     print(f"\nContacts with email {email_to_find} found:")
# #     for contact in found_contacts_by_email:
# #         print(contact)
# # else:
# #     print(f"\nNo contacts found with email {email_to_find}")


# # Search contact by address
# # address_to_find = "125 MААn Street"
# found_contacts_by_address = address_book.find_by_address(user_address)

# # if found_contacts_by_address:
# #     print(f"\nContacts with address {address_to_find} found:")
# #     for contact in found_contacts_by_address:
# #         print(contact)
# # else:
# #     print(f"\nNo contacts found with address {address_to_find}")


# # Search contact by birthday
# # birthday_to_find = datetime.strptime("01.01.1990", "%d.%m.%Y").date()
# found_contacts_by_birthday = address_book.find_by_birthday(datetime.strptime("user_data", "%d.%m.%Y").date())

# # if found_contacts_by_birthday:
# #     print(f"\nContacts with birthday {birthday_to_find.strftime('%d.%m.%Y')} found:")
# #     for contact in found_contacts_by_birthday:
# #         print(contact)
# # else:
# #     print(f"\nNo contacts found with birthday {birthday_to_find.strftime('%d.%m.%Y')}")


# # Change contact name
# # Search contact by name (Exsample, "John Doe")
# contact_to_edit = address_book.find("user_name")

# if contact_to_edit:
#     # Change contact name
#     contact_to_edit.name.value = "New Name"

#     # Save changes
#     address_book.edit("user_name", contact_to_edit)

#     # Show all contacts after editing and updating
# #     print("\nAll contacts after editing and updating:")
# #     for contact_info in address_book.iterator(item_number=len(address_book)):
# #         print(contact_info)

# #     print("Contact updated successfully.")
# # else:
# #     print("Contact not found.")


# # Change phone number
# user_name.edit_phone("old_phone_number", "new_phone_number")
# # record2.edit_phone("9876533321", "9995588443")

# # Show all contacts after editing and updating
# # print("\nAll contacts after editing:")
# # for contact_info in address_book.iterator(item_number=len(address_book)):
# #     print(contact_info)


# # Change contact address
# # Search contact by name (Exsample, "John Doe")
# contact_to_edit = address_book.find("user_name")

# if contact_to_edit:
#     # Change contact address
#     contact_to_edit.edit_address("user_address")

#     # Save changes
#     address_book.edit("user_name", contact_to_edit)

#     # Show all contacts after editing and updating
# #     print("\nAll contacts after editing and updating:")
# #     for contact_info in address_book.iterator(item_number=len(address_book)):
# #         print(contact_info)

# #     print("Address updated successfully.")
# # else:
# #     print("Contact not found.")


# # Change Birthday of contact
# # Search contact by name (Exsample, "Jane Doe")
# contact_to_edit = address_book.find("user_name")

# if contact_to_edit:
#     # Change Birthday of contact
#     new_birthday = "user_data"
#     contact_to_edit.edit_birthday(new_birthday)

#     # Save changes
#     address_book.edit("user_name", contact_to_edit)

# #     # Show all contacts after editing and updating
# #     print("\nAll contacts after editing and updating:")
# #     for contact_info in address_book.iterator(item_number=len(address_book)):
# #         print(contact_info)

# #     print("Birthday updated successfully.")
# # else:
# #     print("Contact not found.")


# # Delete contact by name
# # Name contact that deleted
# name_to_delete = "user_name"

# # Delete contact by name
# address_book.delete(name_to_delete)

# # Show all contacts after delete
# # print("\nContacts after deletion:")
# # for contact_info in address_book.iterator(item_number=len(address_book)):
# #     print(contact_info)


# # Delete contact's Birthday
# # Search contact by name (Exsample, "Jane Doe")
# contact_to_edit = address_book.find("user_name")

# if contact_to_edit:
#     # Delete contact's Birthday
#     contact_to_edit.delete_birthday()

#     # Save changes
#     address_book.edit("user_name", contact_to_edit)

#     # Show all contacts after editing and updating
# #     print("\nAll contacts after editing and updating:")
# #     for contact_info in address_book.iterator(item_number=len(address_book)):
# #         print(contact_info)

# #     print("Birthday deleted successfully.")
# # else:
# #     print("Contact not found.")


# # Add/Change/Delete/email
# # Name of concacts that you wnt to add/updating/delete/email
# name_to_edit = "Jane Doe"

# # Search contact by name
# contact_to_edit = address_book.find_by_name(name_to_edit)

# if contact_to_edit:
#     # Add/Change/Delete/email
#     new_email = None
#     # If new_email not None, add new email
#     # If new_email == None, delete email
#     contact_to_edit.email = Email(new_email) if new_email else None

#     # Save changes
#     address_book.edit(name_to_edit, contact_to_edit)

#     # Delete information about contact after Add/Updating/Delete/email
# #     print(f"Email for {name_to_edit} has been added/updated/deleted.")
# #     updated_contact = address_book.find_by_name(name_to_edit)
# #     if updated_contact:
# #         print(f"Updated contact information:\n{updated_contact}")
# #     else:
# #         print(f"Contact with name {name_to_edit} not found.")
# # else:
# #     print(f"Contact with name {name_to_edit} not found.")


# Downloud database from fail with help by DataManager
data_manager.load_data()
