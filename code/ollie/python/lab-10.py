' Lab 10 - Contact List '

' ~~~ Version 1 ~~~ '

contacts = []

with open('contacts.csv', 'r') as file:         # open contacts file and identify keys
    lines = file.read().split('\n')
    keys = lines[0].split(',')

for i in range(1, len(lines)):                  # make list of dicts given data
    value = lines[i].split(',')
    data = dict(zip(keys, value))
    contacts.append(data)

# print(*contacts, sep = "\n")                    # test

' ~~~ Version 2 ~~~ '

# create functions that carry out each CRUD duty using data from user

# crud_contacts = []

def create(contact): 
    contact = {}

    name = input("New contact's name: ")
    home = input(f"Where does {name.title()} live: ")
    sport = input(f"{name.title()}'s favorite sport: ")

    contact['name'] = name
    contact['home'] = home
    contact['sport'] = sport

    contacts.append(contact)

def retrieve(contact): 
    search = input("Enter the name of the contact you are searching for: ")
    for i in contact:
        if i['name'] == search:
            print(i)

def update(contact):
    choice = retrieve(contact)
    key = input("What key's value would you like changed? (name, home, or sport?): ").lower()
    value = input("What is the new value? ")

    choice[key] = value

def delete():
    pass

while True:
    action = input("""
    ~ CONTACT SETTINGS ~

Action options:
  C - Create a new contact
  R - Retrieve contact info
  U - Update an existing contact
  D - Delete a contact
  V - View contacts
  X - Exit this menu
 
Action: """).lower()
    if action == 'x':
        break
    elif action == 'c':
        contacts.append(create(contacts))
    elif action == 'r':
        retrieve(contacts)
    elif action == 'u':
        update(contacts)
    elif action == 'd':
        delete()
    elif action == 'v':
        print(*contacts, sep = '\n')
    else:
        print("Invalid action, try again!")

update_csv = []
update_csv.append(keys)
for contact in contacts:
    update_csv.append(list(contact.value()))