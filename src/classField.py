# takes the name of the contact
class Field:

    def __init__(self, value):
        self.__value = None
        self.value = value

# This casts the value of the value attribute to a string and returns it
    def __str__(self):
        return str(self.value)

# function that returns a name
    @property
    def value(self):
        return self.__value

# function that assigns a new value
    @value.setter
    def value(self, value):
        self.__value = value
