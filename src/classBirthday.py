from datetime import datetime, date
from classField import Field


class Birthday(Field):
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
