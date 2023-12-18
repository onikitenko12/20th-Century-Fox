from classField import Field

class ContactNote(Field):
    def __init__(self, value):
        if not self.is_valid_note(value):
            raise ValueError("Max length of note with tag is no more than 40 symbols")
        super().__init__(value)

    def is_valid_note(self, value):
        return len(value) <41