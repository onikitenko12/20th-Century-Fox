from classField import Field


# create an email address accoding the Name
class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate(value)

# check correct email
    def validate(self, value):
        # Simple email validation, you can customize as needed
        if '@' in value and '.' in value:
            return value
        else:
            raise ValueError('Invalid email address.')

# This casts the value of the value attribute to a string and returns it
    def __str__(self):
        return f"Email: {self.value}"
