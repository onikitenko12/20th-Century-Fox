from classField import Field


class Address(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate(value)

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Address must be a string.")

    def __str__(self):
        return self.value


# Приклад використання:
# address = Address("123 Main St, City, Country")
# print(address)  # Виведе адресу: 123 Main St, City, Country
