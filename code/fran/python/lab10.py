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
#print(f"lines: {lines}")               ### TEST
header = lines[0].split(',')            # split header into individual items based on comma

for i in range(1,len(lines)):           # loop through all lines except the header
    row = lines[i].split(',')           # split record on comma
    #print(f"row: {row}")               ### TEST
    contact = dict(zip(header,row))     # creates tuple
    # print(f"contact: {contact}")      ### TEST
    contacts.append(contact)            # append individual's dictionary contents to contacts list

#print(f"contacts: {contacts}")       # TEST


# Define create_contact function, which creates a new contact record
def create_contact(contacts):

    user_name = input("What is your first name? ")
    user_fruit = input("What is your favorite fruit? ")
    user_color = input("What is your favorite color? ")

    # Create new dictionary entry
    contacts.append({"name": user_name,"favorite fruit": user_fruit,"favorite color": user_color})
    
    #print(f"contacts, with new record: {contacts}")      ### TEST


# Define retrive_contact function, which retrieves an existing contact record
def retrieve_contact(contact_name, contacts):

    # Search through dictionaries for contact record, based on name key
    for contact in contacts:
        
        #print(f"contact name to search for: {contact_name}")   ### TEST
        #print(contact['name'])                 ### TEST

        if contact['name'] == contact_name:
            found_contact = contact
            break
            #print(f"name found: {contact}")    ### TEST
        else:
            found_contact = []
            #print("not this record")           ### TEST

    return found_contact


# Define update_contact function, which updates an existing contact record
def update_contact(user_name, contacts, update_key, update_value):

    # Find existing contact record
    existing_contact = retrieve_contact(user_name, contacts)

    # Update attribute value for the given attribute key for this contact record
    existing_contact[update_key] = update_value

    #print(f"contacts after update: {contacts}")    ### TEST

# Define delete_contact function, which deletes an existing contact record
def delete_contact(user_name, contacts):

    # Find existing contact record
    existing_contact = retrieve_contact(user_name, contacts)
    #print(f"existing contact: {existing_contact}")     ### TEST

    for index, contact_dict in enumerate(contacts):   
        # print(index, contact_dict)                    ### TEST
        if contact_dict["name"] == user_name:
            del contacts[index]

    # Delete contact record from dictionary
    # del existing_contact['name']
    # del existing_contact['favorite fruit']
    # del existing_contact['favorite color']
    
    #print(f"contacts after delete: {contacts}")  ### TEST


# REPL loop. Prompt user to create, view, modify, or delete a contact record, then execute the action
while True:
    user_action = input("What would you like to do? Enter 'c' to create a new contact, 'r' to retrieve a contact record, 'u' to update an existing contact record, 'd' to delete an existing contact record, or 'exit' to exit: ")

    if user_action == 'c':      
    
        create_contact(contacts)
    
    elif user_action == 'r':    
        # Prompt user for contact name to search on
        user_name = input("What is the first name for the contact record you wish to view? ")
        
        found_contact = retrieve_contact(user_name, contacts)

        #print(f"found contact: {found_contact}")   ### TEST

    elif user_action == 'u':
        # Prompt user for contact info to search on and update
        user_name = input("What is your first name? ")
        user_attribute = input("What attribute would you like to update? fruit or color? ")
        user_attribute_value = input("What is your new favorite fruit or color? ")

        if user_attribute == 'fruit':
            user_attribute = 'favorite fruit'
        elif user_attribute == 'color':
            user_attribute = 'favorite color'

        update_contact(user_name, contacts, user_attribute, user_attribute_value)

    elif user_action == 'd':
        # Prompt user for contact name for record they want to delete
        user_name = input("What is the first name for the contact record you wish to delete? ")

        delete_contact(user_name, contacts)

    elif user_action == 'exit':
        break

# Write contents of post-CRUD dictionary to csv file
# First, create header record
with open('contacts_lab10_output.csv', 'w') as file:
    file.write(f'name,favorite fruit,favorite color\n')  

# Now populate the file with the individual contact info dictionaries
with open('contacts_lab10_output.csv', 'a') as file:
    for contact in contacts:
        line = f"{contact['name'],contact['favorite fruit'],contact['favorite color']}\n"
        line = line.replace("(","")
        line = line.replace(")","")
        line = line.replace("'","")
        line = line.replace(" ","")
        file.write(line)
