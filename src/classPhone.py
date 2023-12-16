
from classField import Field   # Імпортуємо клас Field
import re

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        try:
            if self.value is not None and not re.match(r'^\d{10}$', str(self.value)):
                raise ValueError("Недійсний формат номера телефону. Він повинен містити 10 цифр.")
        except ValueError as e:
            print(f"Помилка валідації: {e}")
            self.value = None

