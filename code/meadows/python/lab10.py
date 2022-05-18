import math
import re
#-------------------------------------------------VERSION 3 ---------------------------------------------------------------#
contact = []

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
csv_tansfer() #using . extend to put the conact inside of the list without adding an entirely new list ontop of the list of lists



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
    return contact

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
# for x in no:
def poof(contact):
    del_enter = input('\nEnter contact to destroy: ')            # used to fully delete a contact if needed from the contact list
    for person in contact:
        if person['name'] == del_enter:
            del person['name']
            del person['state']
            del person['number']
            print('\nPOOF.. gone')
            return contact


def csv_upload(contact):                            # Created a Def to have my function continue to loop through until all things are fixed as needed for a CSV file 
    csv_write = []
    for items, lists in enumerate(contact):     # made this to get the first line ( keys ) only then break so it didn't continue adding it over and over since all of them have name, state, num
        csv_write.append(list(lists.keys()))
        break
    for items, lists in enumerate(contact):    # a continue loop till all contacts have been fully changed over to a CSV format ..... # used enmurate since everything was already set as a list(dict) and it would pull the word and not just the range or length
        csv_write.append(list(lists.values()))   
    csv_write = '\n'.join([','.join(line) for line in csv_write])    
    return csv_write
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


list(filter(None, contact))
print(csv_upload(contact))
with open('contact.csv', 'w') as f:
        f.write(csv_upload(contact))

# csv_write.append(list(lists.keys()))
# csv_upload(contact)
# csv_write = []

# for items, lists in enumerate(contact, 0):
#     if items == 0:
#         csv_write.append(list(lists.keys()))
#         csv_write.append(list(lists.values()))
    
# csv_write = '\n'.join([','.join(line) for line in csv_write])
# with open('contacts.csv', 'w') as f:
#     f.write(csv_write)