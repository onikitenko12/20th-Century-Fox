
from classField import Field
import re

class Mail(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate()

    def validate(self):
        try:
            if self.value is not None and not re.match(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', str(self.value)):
                raise ValueError("Invalid email address format. He must xxx@xxx.xxx ")

        except ValueError as e:
            print(f"Validation error: {e}")
            self.value = None

