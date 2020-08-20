from contact import Contact
from phonebook import Phonebook

if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    thomas = Contact('Thomas', 'Anderson', '+3123398810902', favourite_contact=True, telegram='@Neo', email = 'neo@matrix.zeon')

    contacts = Phonebook('Моя телефонная книга')

    contacts.add_contact(jhon)
    contacts.add_contact(thomas)

    contacts.view()
    contacts.search_favourite()
    contacts.main_search('Thomas', 'Anderson')
    contacts.delete_contact("+71234567809")
    contacts.view()