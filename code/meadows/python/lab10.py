import math
import re
#-------------------------------------------------VERSION 3 ---------------------------------------------------------------#
contact = []
og_c = []
# with open('contacts.csv', 'r') as f:
#     contents = f.read().split('\n')

# for spot in contents:
#     og_c.append(spot.split(','))

# print(a)




def create(contact):
    contacts = {}
    name = input('Name: ').lower()
    contacts['name'] = name
    state = input('state: ').lower()
    contacts['state'] = state
    number = input(r'enter phone number: ')
    contacts['number'] = number
    contact.append(contacts)
    return contact

def info(contact):
    enter = input('\nEnter Name for contact "INFO": \n').lower()
    for person in contact:
        if person['name'] == enter:
            print(person)
            return contact

def update(contact):
    enter = input('\nEnter Name for contact "UPDATE": ')
    update = input('\nChoose 1 to update ( NAME , STATE , NUMBER ): \n').lower()
    for person in contact:
        if person['name'] == enter:
            print(f'\n{person}')
            if 'number' in update:
                n = input('enter new number: ')
                person['number'] = n
                return contact
            if 'state' in update:
                s = input('enter new state: ')
                person['state'] = s
                return contact
            if 'name' in update:
                nm = input('update name: ')
                person['name'] = nm
                return contact
# for x in no:
def poof(contact):
    del_enter = input('\nEnter contact to destroy: ')
    for person in contact:
        if person['name'] == del_enter:
            del person['name']
            del person['state']
            del person['number']
            print('\nPOOF.. gone')
            return contact

# print(poof(update(info(create(contact)))))
play = True
while play:
    phone = input('''
    Enter 1 for create
    Enter 2 for info
    Enter 3 for update
    enter 4 for remove
    enter 5 to STOP

    ENTER CHOICE!: ''').lower()

    if phone == '1':
        create(contact)
    elif phone == '2':
        info(contact)
    elif phone == '3':
        update(contact)
    elif phone == '4':
        poof(contact)
    elif phone == '5':
        print('UPDATING MATRIX...kkrreeshhh...beep..*dial up noises*..')
        break
    else:
        print('\nfor english press the num..bb.rrrr.. for espon... SORRY! please enter a correct input!')
print(contact)

with open('test.csv', 'r') as f:
    contents = f.read().join('\n')