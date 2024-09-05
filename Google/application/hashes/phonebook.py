"""
Given n names and phone numbers, assemble a phone book that maps friends'
 names to their respective phone numbers. You will then be given an unknown
 number of names to query your phone book for. For each name queried, print the
 associated entry from your phone book on a new line in the form name=phoneNumber;
 if an entry for name is not found, print Not found instead.
 inputs:
 n:int ---> number of enteries in phonebook.
 space separated values: first value -->name, second value -->8-digits phone number
 output: phonebook object
"""


class PhoneBook:
    def __init__(self):
        self.phone_numbers = {}

    def save_number(self):
        self.number = int(input())
        self.number = input()
        self.key = self.number.split(" ")[0]
        self.value = self.number.split(" ")[1]
        self.phone_numbers["self.key"] = self.value

    def find_number(self, names: list) -> str:
        self.names = names
        for i in range(len(self.names)):
            if names[i] in self.phone_numbers.keys():
                return self.phone_numbers["name"]
            else:
                return "Not found"

    # @staticmethod
    # def value_len(value):
    #     if len(str(value)) > 8:
    #         return "contact exceeded limit: 8"
    #     else:
    #         return value

    def delete_number(self, key):
        del self.key


phone_book = PhoneBook()
phone_book.save_number()

