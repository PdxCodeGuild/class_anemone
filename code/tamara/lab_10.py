def dict_keys(file_name): # create function to get the keys for the list

    with open(file_name, 'r') as file:
        lines = file.read().split('\n')

    keys = lines.pop(0).split(',')

    return keys

def contacts(file_name): #create a function that returns a list of dict of contacts with a given file_name

    with open(file_name, 'r') as file:
        lines = file.read().split('\n')

    keys = lines.pop(0).split(',') # create a key list to reference, split so that each key has its own index
        # keys[0] is name keys[1] is favorite fruit and keys[2] is favorite 
        # didn't use key function because I need the lines variable

    contacts_list = []

    for item in lines:
        contacts_list.append(item.split(','))

    contacts_list_dict = []

    for a, b, c in contacts_list:
        contacts_list_dict.append({keys[0]: a, keys[1]: b, keys[2]: c})

    return contacts_list_dict 

# create functions for CRUD

def create_record(contacts_list_dict, file_name): #function to add user to a contacts_list_dict and uses the file_name for the keys

    keys = dict_keys(file_name)

    name = input("\nenter the person's name you want added: ")
    fruit = input("\nenter their favorite fruit: ")
    color = input("\nenter their favorite color: ")

    contacts_list_dict.append({keys[0]: name, keys[1]: fruit, keys[2]: color})

    return contacts_list_dict

def retrieve_record(contacts_list_dict): # this function doesn't need the keys
    
    name = input("\nenter the name of the person who's record you would like to view: ")

    for contact in contacts_list_dict:
        for item in contact:
            if contact[item] == name:
                print(f'\nThe record for {name} is: {contact}')

                return name # returning the name of the person they looked for so I can use this in the update_record function

def update_record(contacts_list_dict, file_name): # this one does need keys so needs the file name too

    keys = dict_keys(file_name)

    name = retrieve_record(contacts_list_dict)
    attribute = input(f"\nWhat attribute would you like to change for {name} ?\nYour options are: {keys} ")
    value = input(f"\nWhat is the new value you would like for {attribute}? ")

    for contact in contacts_list_dict:
        for item in contact:
            if contact[item] == name:
                contact[attribute] = value
    
    print(f"\nThe records have been updated\nThe new record is {contacts_list_dict}")
    return contacts_list_dict 

def delete_record(contacts_list_dict): # function to delete a record

    name = input("\nenter the person's name of the record you want deleted: ")

    for contact in contacts_list_dict:
        for item in contact:
            if contact[item] == name:
                contacts_list_dict.remove(contact)

    return contacts_list_dict

def contact_crud_repl(file_name): #create a function to run all of the functions for a CRUD REPL

    contact_list_dict = contacts(file_name)

    while True:
        choice = input("Your record is ready for some changes!\nType 'c' to create a new contact: \nType 'v' to view a contact's record: \nType 'u' to update a record: \nType 'd' to delete a contact: \nType 'done' to exit the program and save your changes: ")
        
        if choice == 'done':
            break
        elif choice == 'v':
            retrieve_record(contact_list_dict)
        elif choice == 'u':
            contact_list_dict = update_record(contact_list_dict, file_name)
        elif choice == 'd':
            contact_list_dict = delete_record(contact_list_dict)
        elif choice == 'c':
            contact_list_dict = create_record(contact_list_dict, file_name)
        else:
            print("\nThat was not a valid entry please try again: ")

    return contact_list_dict

file_name = 'contacts.csv'
keys = dict_keys(file_name)
contact_list_dict = contact_crud_repl(file_name)
line_1 = ''

for key in keys: #create the first line of the csv file
    line_1 += f'{key},'

for item in contact_list_dict: #add the other lines of the csv file
    line_1 += '\n' + item['name'] + ','
    line_1 += item['favorite fruit'] + ','
    line_1 += item['favorite color']

with open(file_name, 'w') as file: #overwrite the info on the csv file
        file.write(line_1)
