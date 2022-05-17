import re
list_of_list = []
contacts = []

#Importing the code snippets from the assignment
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    for line in lines:
        individual_items = line.split(',')
        list_of_list.append(individual_items)

#print(list_of_list)        

keys = list_of_list.pop(0)
#Now that I have my list of lists I need to combine them to form their respective dictionary entries using the header with the other positions


for item in list_of_list:
    dict_1 = dict(zip(keys, item))
    contacts.append(dict_1)
   


def contacts_create(data, keys):
    new_contact = {}
    for key in keys:
        new_contact[key] = input(f'What is your new contact {key}?')
    data.append(new_contact)
 
def contacts_delete(data, keys):
    result = contacts_read(data, keys)
    confirmation = input(f'Are you sure you want to delete {result}?')
    if confirmation == 'yes':
        data.remove(result)

def contacts_update(data, keys):
    result = contacts_read(data, keys)

    key_to_update = input (f"Which key would you like to update? {keys}")
    value_to_update = input(f'what do youw ant to change {value_to_update} to?')
    result[key_to_update] = value_to_update    



def contacts_read(data, keys):
    name = input("What is your contact's name?")
    for contact in data:
        if contact['name'] == name:
            for key in contact:
                print(f'{key}:{contact[keys]}')
            return contact
   

#Here I am working on my REPL input command structure

def start_menu():
    print(contacts)
    print("Type c to Create a contact")
    print("Type r to Retrieve a contact")
    print("Type u to Update a contact")
    print("Type d to delete a contact")
   


    while True:
        user_input = input("What function would you like to perform?")
        if user_input.upper == "exit":
            break 

        elif user_input == 'help':
            start_menu()

    
        elif user_input == "d" :
            name_delete = input('Enter the name of the contact you want to delete')
            contacts_delete(data, keys)

        elif user_input == "u" :
            contact_update = input('Enter the name of the contact you want to update')
            contacts_update(data, keys)


        elif user_input == "r" : 
            retrieve_name = input('Enter the name of the contact you want to retreive: ')
            contacts_read(data, keys)

        elif user_input == "c" :
            contacts_create(data, keys)

data_csv_out = []
data_csv_out.append(keys)
for contact in contacts:
    data_csv_out.append(list(contact.values()))

