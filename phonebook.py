
from decorator import decorator


class Phonebook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self,contact):
        self.contacts.append(contact)

    def view(self):
        for index, contact in enumerate(self.contacts):
            print(f'{index+1}. {contact.main_info}')

    def delete_contact(self, phone_number):
        for contact in self.contacts:
            if phone_number in [contact.phone_number]:
                self.contacts.remove(contact)
            else:
                continue

    def search_favourite(self):
        for contact in self.contacts:
            if contact.favourite_contact:
                print(f'{contact.main_info}')
    @decorator
    def main_search(self, name, surname):
        for contact in self.contacts:
            if contact.name == name and contact.surname == surname:
                print(contact)

