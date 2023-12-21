from classField import Field


# create a phone number into the phone book
class Phone(Field):
    def __init__(self, value=None):
        if value is not None:
            value = self.validate(value)
        self.value = value

    def set_phone_number(self, value):
        self.value = self.validate(value)

    def save_phone_number(self):
        pass

# checks the phone number for correct input
    def validate(self, value):
        cleaned_value = ''.join(filter(str.isdigit, value))
        if len(cleaned_value) == 10:
            return cleaned_value
        else:
            raise ValueError('Invalid phone number. Phone should be 10 digits and may contain separators like "-", " ", etc.')

    def __str__(self):
        return f"Phone number: {self.value}"


# # Створюємо об'єкт класу Phone
# phone_instance = Phone("155-456-7890")

# # Виводимо початковий номер телефону
# print(phone_instance)

# # Змінюємо номер телефону за допомогою методу set_phone_number
# phone_instance.set_phone_number("000 065 4321")

# # Виводимо оновлений номер телефону
# print(phone_instance)

# # Зберігаємо номер телефону
# phone_instance.save_phone_number()
