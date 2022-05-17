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

def create_list(contacts):
    new_name = input("Name? ")
    new_fruit = input("Favorite fruit? ")    
    new_color = input("Favorite color? ")
    new_dict = {"name": new_name, "favorite fruit": new_fruit, "favorite color": new_color}
    contacts.append(new_dict)
    return contacts

def retrieve(contacts):
    user_name = input("contact name? ")
    for contact in contacts:
        if contact["name"] == user_name:
            return contact
    else:
        return "Name not found"
    # for index, contact in enumerate(contacts):
    #     if contact['name'] == name:
    #         print(contact)
    # return contacts[index]
    
def update(contacts):
    contact_update = retrieve(contacts)
    user_input = input("Which do you want to update: 'name', 'favorite fruit', 'favorite color'")
    new_attribute = input(f"What do you want to update {user_input} to?")
    contact_update[user_input] = new_attribute
    print(contact_update)
    return contacts
   
    
def delete(contacts):
    contact_delete = retrieve(contacts)
    confirm = input(f"Are you sure: yes or no ")
    if confirm == 'yes':
        contacts.remove(contact_delete)
        return contacts
    elif confirm == 'no':
        return(contacts)

def convert_to_csv(contacts):  #.join
    csv_output = []
    for contact in contacts:
        csv_output.append(list(contact.values()))
    csv_output = [",".join(line) for line in csv_output]
    csv_output = "\n".join(csv_output)
    with open('contacts.csv', 'w') as f:
        f.write(csv_output)



#-----------While loop for user input---------------#

commands = {'1': 'retrieve',
           '2': 'update', 
           '3': 'create new',
           '4': 'delete',
           '5': 'save'}

contacts = list_split()

while True:
    print(commands)
    command = input("Name a command: ")
    if command == '1':
        print(retrieve(contacts))
    elif command == '2':
        update(contacts)
    elif command == '3':
        create_list(contacts)
    elif command == '4':
        delete(contacts)
    elif command == '5':
        break
convert_to_csv(contacts)

    




# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
#]