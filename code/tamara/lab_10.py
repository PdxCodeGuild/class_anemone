# ------------- #

def dict_keys(file_name): # create function to get the keys for the list

    with open(file_name, 'r') as file:
        lines = file.read().split('\n')

    keys = lines.pop(0).split(',')

    return keys

# --------------- #

def contacts(file_name): #create a function that returns a list of dict of contacts with a given file_name

    with open(file_name, 'r') as file:
        lines = file.read().split('\n')

    keys = lines.pop(0).split(',') # create a key list to reference, split so that each key has its own index and remove the first index of the lines list
        # keys[0] is name keys[1] is favorite fruit and keys[2] is favorite 
        # didn't use key function because I need the lines variable

    lines.pop() # removes last empty '' item on list

    contacts_list = []

    for item in lines:
        contacts_list.append(item.split(','))

    contacts_list_dict = []

    for a, b, c in contacts_list:
        contacts_list_dict.append({keys[0]: a, keys[1]: b, keys[2]: c})

    return contacts_list_dict 

# ------------------------- #

# Implement a CRUD REPL

# create functions for CRUD

def create_record(contacts_list_dict, file_name): #function to add user to a contacts_list_dict and uses the file_name for the keys

    keys = dict_keys(file_name)

    name = input("enter the person's name you want added: ")
    fruit = input("enter their favorite fruit: ")
    color = input("enter their favorite color: ")

    contacts_list_dict.append({keys[0]: name, keys[1]: fruit, keys[2]: color})

    # print(contacts_list_dict) # can be deleted used to check to make sure its working properly

    return contacts_list_dict

# -------------- #

def retrieve_record(contacts_list_dict): # this function doesn't need the keys
    
    name = input("enter the name of the person who's record you would like to view: ")

    for contact in contacts_list_dict:
        for item in contact:
            if contact[item] == name:
                print(f'The record for {name} is: {contact}')

                return name # returning the name of the person they looked for so I can use this in the update_record function

# ------------ #

def update_record(contacts_list_dict, file_name): # this one does need keys so needs the file name too

    keys = dict_keys(file_name)

    name = retrieve_record(contacts_list_dict)
    attribute = input(f"\nWhat attribute would you like to change for {name} ?\nYour options are: {keys} ")
    value = input(f"\nWhat is the new value you would like for {attribute}? ")

    for contact in contacts_list_dict:
        for item in contact:
            if contact[item] == name:
                contact[attribute] = value
    
    print(f"The records have been updated\nThe new record is {contacts_list_dict}")
    return contacts_list_dict # I am not sure if this is the right thing to return yet

# ----------------- #

def delete_record(contacts_list_dict): # function to delete a record can add a while true loop to it

    name = input("enter the person's name of the record you want deleted: ")

    for contact in contacts_list_dict:
        for item in contact:
            if contact[item] == name:
                contacts_list_dict.remove(contact)

    print(contacts_list_dict) # can delete this, using it to check accuracy

    return contacts_list_dict

def contact_crud_repl(file_name):

    contacts_list_dict = []

    contact_list_dict = contacts(file_name) 
    contact_list_create = create_record(contact_list_dict, file_name)
    retrieve_record(contact_list_create)
    contact_list_update = update_record(contact_list_create, file_name)
    contact_list_delete = delete_record(contact_list_update)

    contacts_list_dict = contact_list_delete

    return contacts_list_dict

#     while True:
#         print(f"\nThe current record is {contacts_list_dict}\n")
#         user_choice = input("Would you like to create a new contact to add to the record (y/n)? ")
#         if user_choice == 'n':
#             break
#         else:
#             contacts_list_dict = create_record()

file_name = 'contacts.csv'

contact_crud_repl(file_name)

# TOMORROW --- need to turn each function in CRUD into a REPL and then do version 3