from collections import UserDict
from classRecord import Record


class ContactBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, value):
        flag = 1
        for item in self.data.items():
            if value in str([item[1].name.value, item[1].phones, str(item[1].birthday.value)]):
                flag = 0
                print(f"Contact name: {item[1].name.value}, phones: {'; '.join(p.value for p in item[1].phones)}", f", birthday: {str(item[1].birthday.value)}" if str(item[1].birthday.value) != "None" else "", sep = "")
        if flag:
            print("No matches found") 

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"The contact {name} deleted.")
        else:
            print(f"The contact {name} not found.")

    def add(self, name, address):
        self.data[name] = address

    def __str__(self) -> str:
        return str(self.data)

    def __iter__(self):
        return iter(self.data.values())

    def iterator(self, n):
        counter = 0
        result = ''
        for record in self.data.values():
            result += f"{record}\n"
            counter += 1
            if counter >= n:
                yield result
                counter = 0
                result = ''
        yield result

   
