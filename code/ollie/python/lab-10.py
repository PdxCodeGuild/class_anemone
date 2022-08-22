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

# print(*contacts, sep = "\n")                  # test

' ~~~ Version 2 ~~~ '

# create functions that carry out each CRUD duty using data from user

def create(contact): 
    contact = {}

    name = input("New contact's name: ")
    home = input(f"Where does {name.title()} live: ")
    sport = input(f"{name.title()}'s favorite sport: ")

    contact['name'] = name
    contact['lives in'] = home
    contact['favorite sport'] = sport

    contacts.append(contact)

def retrieve(contact): 
    search = input("Enter the name of the contact you are searching for: ")
    for i in contact:
        if i['name'] == search:
            return(i)

def update(contact):
    choice = retrieve(contact)
    key = input("What key's value would you like changed?\n('name', 'lives in', or 'favorite sport'): ").lower()
    value = input("What is the new value? ")

    choice[key] = value

def delete(contact):
    choice = retrieve(contact)
    print(choice)
    proceed = input("Enter 'yes' to confirm contact deletion: ").lower()
    if proceed == 'yes':
        contact.remove(choice)

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
        create(contacts)
    elif action == 'r':
        print(retrieve(contacts))
    elif action == 'u':
        update(contacts)
    elif action == 'd':
        delete(contacts)
    elif action == 'v':
        print(*contacts, sep = '\n')
    else:
        print("Invalid action, try again!")

csv_info = []
csv_info.append(keys)
for contact in contacts:
    csv_info.append(list(contact.values()))

csv_info = "\n".join([",".join(row) for row in csv_info])

with open('contacts.csv', 'w') as f:
    f.write(csv_info)