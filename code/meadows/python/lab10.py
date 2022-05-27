import math
import re
#-------------------------------------------------VERSION 3 ---------------------------------------------------------------#
contact = []

<<<<<<< HEAD
def csv_tansfer():                             # turning the CSV file into a list dict 
    with open('contact.csv', 'r') as f:
        contents = f.read().split('\n')
    book = []
    spots = contents[0].split(',')

    for i in range(1, len(contents)):
        lists = contents[i].split(',')
        book.append(dict(zip(spots, lists)))
        contact.extend(book)
    return book
csv_tansfer()  #using . extend to put the conact inside of the list without adding an entirely new list ontop of the list of lists
=======
with open('contact.csv', 'r') as f:
    contents = f.read().split('\n')
spots = contents[0].split(',')
>>>>>>> 0dcac4f9f250e1793785b869e1907f960be613e2

for i in range(1, len(contents)):
    lists = contents[i].split(',')
    contact.append(dict(zip(spots, lists)))


def create(contact):             # making a new contact and turning it into a list then appending it to the list outside (contact)
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
    enter = input('\nEnter Name for contact "INFO": \n').lower()           # function to get the persons info and display everything , so they can then decide if the contact is correct and needing an update or not or use the info
    for person in contact:
        if person['name'] == enter:
            print(f"\n Name: {person.get('name')}\n State: {person.get('state')}\n Number: {person.get('number')}")
            print(person)
            return person

def update(contact):
    enter = input('\nEnter Name for contact "UPDATE": ')
    update = input('\nChoose 1 to update ( NAME , STATE , NUMBER ): \n').lower()       # updating the contact via what the person would like to input and fix
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

def poof(contact):
    get = info(contact)
    del_enter = input('\nEnter "yes" to destroy: ').lower()           # used to fully delete a contact if needed from the contact list
    if del_enter == 'yes':
            contact.remove(get)
            return contact


                          # Created a Def to have my function continue to loop through until all things are fixed as needed for a CSV file 

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

csv_write = []
csv_write.append(spots)

for c in contact:
    csv_write.append(list(c.values()))
csv_write = '\n'.join([','.join(line) for line in csv_write])
print(csv_write)

with open('contact.csv', 'w') as f:
        f.write(csv_write)