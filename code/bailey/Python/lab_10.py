'''
Class Anemone
Lab 10
Bailey Baker
'''


contacts = []

# Open CSV file and convert contents to list of dictionaries
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    header = lines[0].split(',')
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(header,row))
        contacts.append(contact)

# Function to create one new contact with all attributes chosen by user input
def create(contacts):
    contact = []
    name = input('Please enter name: ')
    fruit = input('Please enter fruit: ')
    color = input('Please enter color: ')

    contact.append(name)
    contact.append(fruit)
    contact.append(color)
    contact = dict(zip(header, contact))
    contacts.append(contact)
    return contacts

# Function for user to find a contact by their name, returns individual contact
def retrieve(contacts):
    find = input("Enter the name you would like to find: ")
    for contact in contacts:
        if contact['name'] == find:
            return contact

# Function to find a contact by name and update one of their attributes
def update(contacts):
    find = input("Enter the name you would like to find: ")
    for contact in contacts:
        if contact['name'] == find:
            attribute = input("Enter which attribute you would like to change: ")
            if attribute in contact:
                value = input("Enter the new value for the attribute: ")
                contact[attribute] = value
                return contacts

# Function to find contact by name and delete entire contact
def delete(contacts):
    find = input("Enter the name of the contact you would like to delete: ")
    for contact in contacts:
        if contact['name'] == find:
            contacts.remove(contact)

#REPL loop to allow user to choose which function they would like to use to modify CSV file
while True:
    choice = input('''\n\nEnter 'c' to create a record
Enter 'r' to retrieve a record
Enter 'u' to update a record
Enter 'd' to delete a record
Enter 'x' when you are finished

: ''').lower()

    if choice == 'c':
        create(contacts)
    elif choice == 'r':
       find = retrieve(contacts)
       print(find)
    elif choice == 'u':
        update(contacts)
    elif choice == 'd':
        delete(contacts)
    elif choice == 'x':
        break
    else:
        print("Please enter a valid input.")
        
# return contacts to CSV format and write back to CSV file
lines = [','.join(header)]
for contact in contacts:
    row = ','.join(contact.values())
    lines.append(row)
final = '\n'.join(lines)

with open('contacts.csv', 'w') as file:
    file.write(final)

