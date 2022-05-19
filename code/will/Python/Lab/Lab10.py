import re
from unicodedata import name
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

print('1', contacts)



def contacts_create(contacts, keys):
    new_contact = {}
    for key in keys:
        new_contact[key] = input(f'What is your new contact {key}? ')
    contacts.append(new_contact)
    
 
def contacts_delete(contacts):
 
    #confirmation = contacts_read(contacts)
    confirmation = input(f'Are you sure you want to delete {name}? ')
    if confirmation == 'yes':
        contacts.remove(name)
        

def contacts_update(contacts, name, keys):
    result = contacts_read(contacts, name)

    key_to_update = input (f"Which key would you like to update? {keys} ")
    value_to_update = input(f'what do you want to change {key_to_update} to? ')

    result[key_to_update] = value_to_update  
    print(contacts)  
    return contacts



def contacts_read(contacts, name):
    for contact in contacts:
        if contact['name'] == name:
            # for key in contact:
            #    print(f'{key}:{contact[keys]}')
            return contact
   

#Here I am working on my REPL input command structure

def start_menu():
    #print(contacts)
    print("Type c to Create a contact")
    print("Type r to Retrieve a contact")
    print("Type u to Update a contact")
    print("Type d to delete a contact")
   


    while True:
        user_input = input("What function would you like to perform? ")
        if user_input.upper == "exit":
            break 

        elif user_input == 'help':
            start_menu()

    
        elif user_input == "d" :
            name = input('Enter the name of the contact you want to delete ')
            contacts_delete(name)
            

        elif user_input == "u" :
            name = input('Enter the name of the contact you want to update ')
            contacts_update(contacts, name, keys)
            


        elif user_input == "r" : 
            name = input("What is your contact's name? ")
            print(contacts_read(contacts, name))
            
            

        elif user_input == "c" :
            contacts_create(contacts, keys)
            print(contacts)
            

data_csv_out = []
data_csv_out.append(keys)
for contact in contacts:
    data_csv_out.append(list(contact.values()))

start_menu()