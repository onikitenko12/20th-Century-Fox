from classField import Field


class Email(Field):
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
