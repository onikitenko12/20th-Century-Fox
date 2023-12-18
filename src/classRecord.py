
from classField import Field
from classBirthday import Birthday
from classMail import Email
from classPhone import Phone
from classContact import Name
from classContactNotes import ContactNote


class Record(Field):
    def __init__(self, name, birthday=None, email=None):
        self.name = Name(name)
        self.phones = []
        self.notes = []
        self.birthday = Birthday(birthday) if birthday else None
        self.email = Email(email) if email else None

    def __str__(self):
        return f"Contact name: {self.name.value}, \
                phones: {'; '.join(p.value for p in self.phones)}" \
               f", birthday: {self.birthday.value}, {self.email}" \
                if self.birthday else ""
    
    def add_note(self, note_text: str):
        note = ContactNote(note_text)
        note.is_valid_note(note_text)
        if note not in self.notes:
            self.notes.append(note)
    
    def remove_note(self, note_to_remove):
        is_found_note = False
        for item in self.notes:
            if item.value == note_to_remove:
                self.notes.remove(item)
                is_found_note = True
                break
        if not is_found_note:
            raise ValueError('Note not found')
        
    def find_note(self, note_text:str):
        is_found_note = False
        for note in self.notes:
            if note.value.find(note_text) != -1:
                is_found_note = True
                return note
        if not is_found_note:
            raise ValueError('Note not founded')

    def get_all_notes(self):
        result = [n.value for n in self.notes]
        return result
    
    def add_tag(self, tag, note_text):
        is_found_note = False
        for index, item in enumerate(self.notes):
            if item.value == note_text:
                self.notes[index] = ContactNote(f"<{tag}>{note_text}")
                is_found_note = True
        if not is_found_note:
            raise ValueError('Note not founded')
        
    def remove_tag(self, tag_to_remove):
        for item in self.notes:
            if item.value.find(tag_to_remove) != -1:
                item.value = item.value.removeprefix(f"<{tag_to_remove}>")
                return 
        raise ValueError(f'Tag {tag_to_remove} not founded')

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if not any(existing_phone.value == phone.value for
                   existing_phone in self.phones):
            self.phones.append(phone)

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                try:
                    phone.validate(new_phone)
                    phone.value = new_phone
                    return new_phone
                except ValueError as e:
                    print(e)
        raise ValueError(f"Phone number {old_phone} not found.")

    def delete_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return phone.value
        raise ValueError(f"Phone number {phone_number} not found.")

    def days_to_birthday(self):
        if self.birthday:
            return self.birthday.days_until_next_birthday()
        return None
