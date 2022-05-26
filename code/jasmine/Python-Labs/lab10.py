
# Contact List Lab
# Class Example

import re
from turtle import update

with open ('contact.csv', 'r') as f:
    data_csv = f.read()

# csv_lines = data_csv.split("\n")
# list_of_lists = []
# for line in csv_lines:
#     list_of_lists.append(line.split(','))
list_of_lists = [line.split(',') for line in data_csv.split('\n')]

keys = list_of_lists[0]
## empty ist
# d
# for row in list_of_lists[1::]:
#     #empty dict for each row
#     row_dict = {}
#     for i in range(len(row)):
        
#         row_dict[keyd
#[i]] = row[i]
        # row_dict['name'] = 'jasmine'
        # row_dict['favorite color'] = 'purple'
        # row_dict['favorite fruit'] = 'mango'
    # print(row_dict)
# for values in list_of_lists[1::]:
#     contacts.append(dict(zip(keys,values)))
# # print(contacts)

contacts = [dict(zip(keys,values)) for values in list_of_lists[1::]]

def create_contact(data, keys):
    # new_contact = {}
    # for key in keys:
    #     new_contact[key] = input(f"What is your new contact's {key}?")
    # data.append(new_contact)

    ##dict comprehension
    data.append({key:input(f"What is your new contact's {key}?") for key in keys})

def read_contact(data,keys):
    # result = "you found me"
    # return result
    ##Which contact do you want to search
    # name = input("What is your contact's name? ")
    # ##look for that name
    # for contact in data:
    #     if contact['name'] == name:
           
    #         print(contact)
    #         return contact
    key_string = "\n" + "\n".join(keys) + "\n"
    key_input = input(f'What would you like to search by? Choose from: {key_string}')
    contact_input = input("What is your search term? ")

    # data_results = []
    # for contact in data:
    #     if contact[key_input] == contact_input:
    #         data_results.append(contact)
    data_results = list(filter(lambda contact: contact[key_input] == contact_input, data))

    print(data_results)
    return data_results   

def update_contact(data,keys):
    # result = read_contact(data,keys)
    # # update the result
    # key_to_update = input(f'What key would you like to update? {keys}')
    # value_to_update = input(f'What do you want to change {key_to_update} to? ')
    # result[key_to_update] == value_to_update

    data_results = read_contact(data, keys)

    index_to_update = int(input(f"Which contact would you like to edit? (1-{len(data_results)}) ")) - 1
    key_to_update = input(f"What key would you like to update? {keys} ")
    value_to_update = input(f"What do you want to change {key_to_update} to? ")
    data_results[index_to_update][key_to_update] = value_to_update




def delete_contact(data,keys):
    # result = read_contact(data,keys)
    # #delete the result
    # confirmation = input(f"Are you sure you want to delete? (result['name'])")

    # if confirmation.lower() in ['y', 'yes']:
    #     data.remove(result)
    data_results = read_contact(data, keys)

    index_to_delete = int(input(f"Which contact would you like to delete? (1-{len(data_results)}) ")) - 1
    data.remove(data_results[index_to_delete])

while True:
    # print(contacts)
    user_input=input("What would you like to do? (c)reate, (r)ead, (u)pdate, (d)elete, (q)uit > ")
    if user_input.lower() in ['q', 'quit', 'exit']:
        break
    elif user_input == 'c':
        create_contact(contacts,keys)
    elif user_input == 'r':
        read_contact(contacts,keys)
    elif user_input == 'u':
        update_contact(contacts,keys)
    elif user_input == 'd':
        delete_contact(contacts,keys)

data_csv_out = []
data_csv_out.append(keys)
for contact in contacts:
    data_csv_out.append(list(contact.values()))



output = []
for row in data_csv_out:
    output.append(",".join(row))

## list
final_output = "\n".join(output)



with open('contact.csv', 'w') as file:
    file.write(final_output)

print(final_output)

