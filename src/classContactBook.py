from collections import UserDict
from classRecord import Record


class ContactBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        for record_name, record in self.data.items():
            if record_name == name:
                return record
        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"The contact {name} deleted.")
        else:
            print(f"The contact {name} not found.")

    def add(self, name, address):
        self.data[name] = address

    def iterator(self, item_number):
        counter = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {record}\n'
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ''
