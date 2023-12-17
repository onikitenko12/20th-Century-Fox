from collections import UserDict
from datetime import datetime, timedelta
import re
import pickle

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birhday = Birthday(birthday)

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        birthday_str = f", день народження: {self.birthday}" if self.birthday.value else ""
        return f"Контактна особа: {self.name}{birthday_str}, телефони: {phones_str}"

    def days_to_birthday(self):  # кількість днів до наступного дня народження
        if self.birthday.value:
            today = datetime.now()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day)
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, self.birthday.value.month, self.birthday.value.day)
            days_left = (next_birthday - today).days
            return days_left
        return None

    def contacts_with_upcoming_birthdays(self, days):  # список контактів, у яких день народження через задану кількість днів від поточної дати
        today = datetime.now()
        upcoming_contacts = []

        days_to_birthday = self.days_to_birthday()
        if days_to_birthday is not None and 0 < days_to_birthday <= days:
            upcoming_contacts.append(self)
        return upcoming_contacts


    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = Birthday(value)



