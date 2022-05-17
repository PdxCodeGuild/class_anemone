' Lab 10 - Contact List '

' ~~~ Version 1 ~~~ '

# contacts = []

# with open('contacts.csv', 'r') as file:         # open contacts file and identify keys
#     lines = file.read().split('\n')
#     keys = lines[0].split(',')

# for i in range(1, len(lines)):                  # make list of dicts given data
#     value = lines[i].split(',')
#     data = dict(zip(keys, value))
#     contacts.append(data)

# print(contacts)

' ~~~ Version 2 ~~~ '

# create functions that carry out each CRUD duty using data from user

contacts = []

def create(contact):
    contact = []
    contact.append(input("New contact's name: ").lower())
    contact.append(input("Where new contact lives: ").lower())
    contact.append(input("New contact's favorite sport: ").lower())
    data = dict(zip(, contact))
    contact.append(data)
    return contact

# def retrieve(contact): 
#     search = input("Enter the name of the contact you are searching for: ")

