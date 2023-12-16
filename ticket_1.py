from collections import UserDict
from datetime import datetime, date


class Pearson:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __str__(self):
        return str(self.value)


class Name(Pearson):
    pass


class Phone(Pearson):
    def __init__(self, value):
        self.value = self.validate(value)

    def validate(self, value):
        cleaned_value = ''.join(filter(str.isdigit, value))
        if len(cleaned_value) == 10:
            return cleaned_value
        elif len(cleaned_value) == 12 and cleaned_value.startswith('+38'):
            return cleaned_value
        else:
            raise ValueError('Invalid phone number. Phone should be 10 or 12 \
                             digits and may start with +38')


class Birthday(Pearson):
    def __init__(self, date):
        self.value = date

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_date):
        if not self.validate_date_format(new_date):
            raise ValueError("Date should be 'dd.mm.yyyy' format.")
        self._value = new_date

    def validate_date_format(self, date):
        try:
            datetime.strptime(date, '%d.%m.%Y')
            return True
        except ValueError:
            return False

    def days_until_next_birthday(self):
        today = date.today()
        next_birthday = date(today.year, self.value.month, self.value.day)
        if today > next_birthday:
            next_birthday = date(today.year + 1, self.value.month,
                                 self.value.day)
        days_until_birthday = (next_birthday - today).days
        return days_until_birthday


class Email(Pearson):
    def __init__(self, value):
        self.value = self.validate(value)

    def validate(self, value):
        # Simple email validation, you can customize as needed
        if '@' in value and '.' in value:
            return value
        else:
            raise ValueError('Invalid email address.')

    def __str__(self):
        return f"Email: {self._value}"


class Record(Pearson):
    def __init__(self, name, birthday=None, email=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None
        self.email = Email(email) if email else None

    def __str__(self):
        return f"Contact name: {self.name.value}, \
                phones: {'; '.join(p.value for p in self.phones)}" \
               f", birthday: {self.birthday.value}, {self.email}" \
                if self.birthday else ""

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if not any(existing_phone.value == phone.value for
                   existing_phone in self.phones):
            self.phones.append(phone)

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

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

    def remove_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return phone.value
        raise ValueError(f"Phone number {phone_number} not found.")

    def days_to_birthday(self):
        if self.birthday:
            return self.birthday.days_until_next_birthday()
        return None


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        for record_name, record in self.data.items():
            if record_name == name:
                return record
        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"The contact {name} deleted.")
        else:
            print(f"The contact {name} not found.")

    def add(self, name, address):
        self.data[name] = address

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
