from classField import Field


# create a phone number into the phone book
class Phone(Field):
    def __init__(self, value):
        self.value = self.validate(value)

# checks the phone number for correct input
    def validate(self, value):
        cleaned_value = ''.join(filter(str.isdigit, value))
        if len(cleaned_value) == 10:
            return cleaned_value
        elif len(cleaned_value) == 12 and cleaned_value.startswith('+38'):
            return cleaned_value
        else:
            raise ValueError('Invalid phone number. Phone should be 10 or 12 \
                             digits and may start with +38')
