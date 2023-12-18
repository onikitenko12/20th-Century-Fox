# takes the name of the contact
class Field:
    def __init__(self, value):
        self.value = value

# a function that returns a name
    @property
    def value(self):
        return self._value

# function that assigns a new value
    @value.setter
    def value(self, new_value):
        self._value = new_value

# This casts the value of the value attribute to a string and returns it
    def __str__(self):
        return str(self.value)


# class inherits all values ​​of the Field class
class Name(Field):
    pass
