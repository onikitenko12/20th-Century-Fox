from classField import Field


# create an email address accoding the Name
class Email(Field):
    def __init__(self, email):
        self.email = self.validate(email)

# check correct email
    def validate(self, email):
        # Simple email validation, you can customize as needed
        if '@' in email and '.' in email:
            return email
        else:
            raise ValueError('Invalid email address.')

# This casts the value of the value attribute to a string and returns it
    def __str__(self):
        return f"Email: {self.email}"
