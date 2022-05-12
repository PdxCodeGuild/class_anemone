#Lab10
#Manage list of contacts

import re

#Version1
with open ('favorites.csv', encoding="utf-8") as file:
    lines = file.read().split('\n')

contacts = []

contact_list = []
contact_info = {}

for line in lines:   
    contact_list.append(line.split(','))

keys = contact_list.pop(0)

# name = input('Enter you name: ')
# fruit = input('Enter your favorite fruit: ')
# color = input('Enter your favorite color: ')

#Create
def create():
    new_entry = []

    new_entry.append(input('Enter your name: '))
    new_entry.append(input('Enter your favorite fruit: '))
    new_entry.append(input('Enter your favorite color: '))

    contact_list.append(new_entry)

#Retrieve
def retrieve(contacts):
    lookup_name = input('Enter the name of the contact you would like to search: ')
    for contact in contacts:
        if contact['name'] == lookup_name:
            print (contact)
            return contact
        else:
            return ('Name not found.')


#Update
def update(contact):
    ret_contact = retrieve(contact)
    change_value = input('Enter the value you would like to update(name, fruit, or color):')
    if change_value == 'name':
        updated_value = input('You have requested a name change. Enter what you want to change the name to: ')
        contact['name'] = updated_value

    if change_value == 'fruit':
        print ('You have requested a fruit change.')
        
    if change_value == 'color':
        print ('You have requested a color change.')
    print(ret_contact)
        

for i, contact in enumerate(contact_list):
    result = zip(keys, contact_list[i])
    final_result = dict(result)
    contacts.append(final_result)



update(contacts)

#print(contacts)


