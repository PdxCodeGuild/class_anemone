#Lab10
#Manage list of contacts

import csv
import re

#Open CSV file
with open ('favorites.csv', encoding="utf-8") as file:
    lines = file.read().split('\n')

contacts = []

contact_list = []
contact_info = {}

for line in lines:   
    contact_list.append(line.split(','))

keys = contact_list.pop(0)

#Covert lines into list of dicts
for i, contact in enumerate(contact_list):
    result = zip(keys, contact_list[i])
    final_result = dict(result)
    contacts.append(final_result)

#Create: function to create a record
def create(contacts, keys):
    new_entry = []
    new_contact = {}

    new_entry.append(input('Enter your name: '))
    new_entry.append(input('Enter your favorite fruit: '))
    new_entry.append(input('Enter your favorite color: '))

    for i, key in enumerate(keys):
        new_contact[key] = new_entry[i]
    
    contacts.append(new_contact)
    
    return contacts

#Retrieve: function to retrieve a record
def retrieve(contacts):
    lookup_name = input('Enter the name of the contact you would like to search: ')
    for contact in contacts:
        if contact['name'] == lookup_name:
            print (contact)
            return contact
    else:
        return ('Name not found.')


#Update: function to update a record
def update(contact):
    ret_contact = retrieve(contact)
    change_value = input('Enter the value you would like to UPDATE(name, fruit, or color):')
    if change_value == 'name':
        updated_name = input('You have requested a NAME change. Enter what you want to change the name to: ')
        ret_contact['name'] = updated_name
        
    elif change_value == 'fruit':
        updated_fruit = input('You have requested a FRUIT change. Enter what you want to change the fruit to: ')
        ret_contact['favorite fruit'] = updated_fruit
        
    elif change_value == 'color':
        updated_color = input('You have requested a COLOR change. Enter what you want to change the color to: ')
        ret_contact['favorite color'] = updated_color

    return ret_contact

#Delete: function to delete a record
def delete(contact):
    ret_contact = retrieve(contact)
    print(ret_contact)
    del_contact = input('Do you want to DELETE this contact? yes or no? ')
    if del_contact == 'yes':
        contacts.remove(ret_contact)
        return contacts
        # print ('This contact has been DELETED.')

    elif del_contact == 'no':
        print ('This contact has NOT been deleted')


#Ask user what they would like to do
#request = input('What would you like to do? create, retrieve, update, or delete a record? If finished, enter "done": ')
#print requested function
while True:
    request = input('What would you like to do? create, retrieve, update, or delete a record? If finished, enter "done": ')
    if request == 'create':
        create(contacts, keys)
    elif request == 'retrieve':
        retrieve(contacts)
    elif request == 'update':
        update(contacts)
    elif request == 'delete':
        delete(contacts)
    elif request == 'done':
        print ('All done.')
        break
    
#print(contacts)


#print(lines)

updated_contact_list = []
updated_contact_list.append(keys)


for contact in contacts:
    new_values = list(contact.values())
    updated_contact_list.append(new_values)

updated = []
for contact in updated_contact_list:
    updated.append(','.join(contact))

csv_output = '\n'.join(updated)

#print(csv_output)

with open ('favorites.csv', 'w') as f:
    f.write(csv_output)