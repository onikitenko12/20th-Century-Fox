
from classField import Field
import re

class Mail(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        try:
            if self.value is not None and not re.match(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', str(self.value)):
                raise ValueError("Недійсний формат електронної адреси. Він повинен xxx@xxx.xxx ")

        except ValueError as e:
            print(f"Помилка валідації: {e}")
            self.value = None

