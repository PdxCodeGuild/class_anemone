# Lab 10 - Contacts List
# Fran Kappes

# Import regular expression module
import re

# Open and read in contacts csv file
file_name = 'contacts_lab10.csv'

with open(file_name, 'r') as file:
    contents = file.read() 
    print(f"contents: {contents}")  ### TEST


# Create a string of individual contact dictionaries from the contacts file
contacts = []
lines = contents.split('\n')            # split record on new line character
print(f"lines: {lines}")
header = lines[0].split(',')            # split header into individual items based on comma

for i in range(1,len(lines)):           # loop through all lines except the header
    row = lines[i].split(',')           # split record on comma
    print(f"row: {row}")
    contact = dict(zip(header,row))     # creates tuple
    print(f"contact: {contact}")       # TEST
    contacts.append(contact)            # append individual's dictionary contents to contacts list

print(f"contacts: {contacts}")       # TEST

### Notes from discussion with Liz ###

# Need to have REPL (while True loop)
# Pass in contacts dictionary to all functions

##### END NOTES #####

# Prompt user to create, view, modify, or delete a contact record, then execute the action
user_action = input("What would you like to do? Enter 'c' to create a new contact, 'r' to retrieve a contact record, 'u' to update an existing contact record, or 'd' to delete an existing contact record: ")

new_record = []

if user_action == 'c':
    user_name = input("What is your first name? ")
    user_fruit = input("What is your favorite fruit? ")
    user_color = input("What is your favorite color? ")

    # Assemble new record from user input
    new_record = user_name + ',' + user_fruit + ',' + user_color
    print(f"new record: {new_record}")      ### TEST
    
    # Add new record to file
    with open(file_name, 'a') as file:
        file.write(new_record)

elif user_action == 'r':
    user_name = input("What is the first name for the contact record you wish to view? ")

    # Find the record
    #existing_record = contact.split('\n')
    #existing_record = re.findall(r'{user_name}', contact)
    #existing_record = contacts.find(user_name)
    
    # for i in range(1,len(lines)):           # loop through all lines except the header
    #     row = lines[i].split(',')           # split record on comma
    #     print(f"row: {row}")
    #     contact = dict(zip(header,row))     # creates tuple
    #     print(f"contact: {contact}")       # TEST
    #     contacts.append(contact)


    matches = [match for match in lines if user_name in match]
    values = [value for value in contact.values() if user_name in value]  ### RETURNS empty list []
    print(f"matches: {matches}")  ### RETURNS ['bert,banana,blue']
    
    match_name = matches[0]   ### RETURNS bert,banana,blue
    print(f"match name: {match_name}")
    #record = matches.split(',')  ### GET AttributeError: 'list' object has no attribute 'split'
    #print(f"record: {record}")
    # print(f"name: {matches[0]}")
    # print(f"favorite fruit: {matches[1]}")
    # print(f"favorite color: {matches[2]}")
    print(f"values: {values}")
    
    
    # print(f"lines: {lines}")
    # if user_name in lines: #contents:
    #     print("user name exists")
    # else:
    #     print("not found")
    # #print(f"existing record: {existing_record}")



elif user_action == 'u':
    user_name = input("What is your first name? ")
    user_attribute = input("What attribute would you like to update? fruit or color? ")
    user_attribute_value = input("What is your new favorite fruit or color? ")



elif user_action == 'd':
    user_name = input("What is the first name for the contact record you wish to delete? ")





#print(f"contacts list: {contacts}")