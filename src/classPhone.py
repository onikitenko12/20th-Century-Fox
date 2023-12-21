from classField import Field


# create a phone number into the phone book
class Phone(Field):
    def __init__(self, value=None):
        if value is not None:
            value = self.validate(value)
        self.value = value

    def set_phone_number(self, value):
        self.value = self.validate(value)

    # def save_phone_number(self):
    #     pass

# checks the phone number for correct input
    def validate(self, value):
        cleaned_value = ''.join(filter(str.isdigit, value))
        if len(cleaned_value) == 10:
            return cleaned_value
        else:
            raise ValueError('Invalid phone number. Phone should be 10 digits and may contain separators like "-", " ", etc.')

    def __str__(self):
        return f"Phone number: {self.value}"


# # Create object class Phone
# phone_instance = Phone("155-456-7890")

# # Show previous phone number
# print(phone_instance)

# # Change phone number with help of method set_phone_number
# phone_instance.set_phone_number("000 065 4321")

# # Show uploading phone number
# print(phone_instance)

# # Save phone number
# phone_instance.save_phone_number()
