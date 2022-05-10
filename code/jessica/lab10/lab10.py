#------------LAB10 v1, v2, v3---------------------#

def list_split():
    with open('contacts.csv') as f:
        lines = f.read().split("\n")
     
    contacts = []
    header = lines[0].split(",")
    
    for i in range(1, len(lines)):
        row = lines[i].split(",")
        contact = dict(zip(header, row))
        contacts.append(contact)
    return contacts

#-------------CRUD functions v2--------------------#

def create_list():
    new_line = input("Name, Favorite fruit, Favorite color: ")
    new_line = list(new_line.split(","))       
    contacts.append(new_line)
    print(contacts)
    return contacts

def retrieve(contacts, name):
    for index, contact in enumerate(contacts):
        if contact['name'] == name:
            print(contact)
    return contacts[index]
    
def update():
    contact_name = input('Which contact do you want to update? ')
    for contact in contacts:
        if contact_name == contact['name']:
            print(contact)
            update = input('Which attribute would you like to update? ')
            contact[update] = input('Type updated information: ')
            print(contact)
            return contact
    
def delete():
    contact_name = input('Which contact do you want to delete? ')
    for contact in contacts:
        if contact_name == contact['name']:
            confirm = input(f"Are you sure: yes or no ")
            if confirm == 'yes':
                contacts.remove(contact)
            elif confirm == 'no':
                pass
                print(contacts)
                return(contacts)



#-----------While loop for user input---------------#

commands = ['1', 'retrieve',
           '2', 'update', 
           '3', 'create new',
           '4', 'delete',
           '5', 'quit']

contacts = list_split()

while True:
    print(commands)
    command = input("Name a command: ")
    if command == '1':
        name = input("Name? ")
        retrieve(contacts, name)
    elif command == '2':
        update()
    elif command == '3':
        create_list()
    elif command == '4':
        delete()
        print(contacts)
    elif command == '5':
        break
    
    
        



# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
#]