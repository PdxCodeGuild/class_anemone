contact = []

# opens selected file.
with open("contacts.csv", 'r') as file:
    # split the lines in the file
    lines = file.read().split('\n')

    c_list = []
    key = lines[0].split(',')

    contact.append(lines[0].split(','))
    contact.append(lines[1].split(','))
    contact.append(lines[2].split(','))

    for thing in contact:
        con = dict(zip(contact[0], thing))
        c_list.append(con)
    del c_list[0]


# Creates new contact
def create():
    name = input("Enter Contact Name: ")
    address = input("Enter Contact Address: ")
    phone = input("Enter Contact Phone: ")
    add = False
    for contact in c_list:
        if name == c_list:
            print('Name already in list! Please try again.')
        elif contact['name'] == name:
            print('Contact has been created.')
        else:
            add = True
    if add:
        c_list.append({'name': name, 'address': address, 'phone': phone})


# Shows retrieved information
def lists():
    request = input("Enter contact name: ")
    for name in c_list:
        if name['name'] == request:
            print(name)
        # elif name['name'] != request:
        #     print("Name not in present in list. ")


# Updates contact information
def update_contact():
    old_user = input("Enter name of contact to change: ")
    new_user = input("Enter new name of contact: ")
    new_change = input("Enter new address of contact: ")
    for name in c_list:
        if name['name'] == old_user:
            if new_user in name:
                name[new_user] = new_change


# Deletes contact information
def delete():
    user = input("Enter contact to delete? ")
    for name in c_list:
        if name['name'] in user:
            c_list.remove(name)


# Selectable commands
while True:
    print("Select a command: '1': Create, '2': List, '3': Delete, '4': Update, '5': Help, '6':exit")
    command = input("Enter a command: ")

    if command == '1':
        create()

    elif command == '2':
        lists()

    elif command == '3':
        delete()
        print("Contact has been deleted\n")

    elif command == '4':
        update_contact()
        print('Contact has been updated\n')

    elif command == "5":
        print("Available commands")
        print("1  - Create contacts")
        print("2  - List contacts")
        print("3  - Remove contact")
        print("4  - Update contact")
        print("5  - Help")
        print("6  - Exit")

    elif command == '6':
        break
    else:
        print("Key command not permitted, try again!")

with open("contacts.csv", 'w') as file:
    new_contact = []
    added_contact = []
    lists = []
    done = []
    new_contact.append(list(c_list[0].keys()))

    for abso in c_list:
        new_contact.append(list(abso.values()))

    for goto in new_contact:
        lists = ','.join(goto)
        added_contact.append(lists)

    done = '\n'.join(added_contact)
    print(done)

    file.write(done)
