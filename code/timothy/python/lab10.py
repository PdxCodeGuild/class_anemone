# ....Lab 10 Version 1 ~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~

import re

# with open('C:/users/johns/desktop/contact_list.csv', 'r') as file:
#     lines = file.read().split('\n')
#     # print(lines)

# contacts = []

# header =  True
# for line in lines:
#     if header:
#         keys = ''.join(line).split(',')
#         header = False
#     else:
#         values = ''.join(line).split(',')
#         contacts.append({keys[i]:values[i] for i in range(len(keys))})


# print(contacts)

# ....Lab 10 Version 2 ~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~

# CRUD REPL

def csv_crud_repl(file_path, mode):
    with open (file_path, mode) as file:
        lines = file.read().split('\n')

    contacts = []

    header =  True
    for line in lines:
        if header:
            keys = ''.join(line).split(',')
            header = False
        else:
            values = ''.join(line).split(',')
            contacts.append({keys[i]:values[i] for i in range(len(keys))})
    create = input("Do you want to create a new contact? y/n ")
    if create == 'y':
        def create():
            new_values = input('Please state: Name,Favorite Color,Favorite Fruit ')
            new_values = list(new_values.split(','))
            values.append(new_values)
            contacts.append({keys[i]:new_values[i] for i in range(len(keys))})
    elif create == 'n':
        pass
        # print(contacts)
    create() 

    def retrieve():
        display = input("Do you want to retrieve a contact? y/n ")
        if display == 'y':
            contact_name = input('State the name of the contact you want to retrieve: ')
            for elements in contacts:
                if contact_name == elements['name']:
                    print(elements)    
        if display == 'n':
            pass        
    retrieve()

    # def update():
    #     update = input("Do you want to update a contact? y/n ")
    #     if update == 'y':
            

csv_crud_repl('C:/users/johns/desktop/contact_list.csv', 'r')