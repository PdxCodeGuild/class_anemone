'''Contact List'''

# Open and read the csv file 'contacts.csv'
with open('contacts.csv', 'r') as file:
    contact_list = file.read()
    
# Create a list containing contacts
contact_list = [line.split(",") for line in contact_list.split("\n")]

headers = contact_list[0]

# Make a list of contacts to search for through the csv file
# use the zip() function for familiarity purposes
new_list = [dict(zip(headers, values)) for values in contact_list[1::]]

# Create new conact function
# add a new contact by name, favorite fruit and favorite color
def create(new_list, headers):
    new_list.append({header: input(f"What is your contacts {header}? ") for header in headers})
    return new_list

# Create a retrieve contact name function.
# Use headers as search options for contact
def retrieve(new_list, headers):
    header_search = "\n" + "\n".join(headers) + "\n"
    contact_search = input(f"\nWhat would you like to search?  Options are: \n\t{header_search.title()}\n")
    search_input = input(f"Enter {contact_search}: ")

    search_results = list(filter(lambda contact: contact[contact_search] == search_input, new_list))

    print(search_results)

    return search_results

# Update the contacts name, fruit or color
def update(new_list, headers):
    search_results = retrieve(new_list, headers)
    # update a specific index of the contact
    positon_update = int(input(f"What would you like to edit? (1-{len(search_results)}) \n")) - 1
    list_update = input(f"Which header would you like to update? {headers} ")
    item_update = input(f"What would you like their {list_update} to change to? ")

    search_results[positon_update][list_update] = item_update

# Delete a contact function
def delete(new_list, headers):
    search_results = retrieve(new_list, headers)
    positon_delete = int(input(f"What would you like to delete? (1-{len(search_results)}) \n")) - 1
    new_list.remove(search_results[positon_delete])

# Make the REPL for the program and write to the CSV file.
while True:
    user_input = input("(C)reate, (R)etrieve, (U)pdate or (D)elete. \n")
    if user_input == 'q':
        break
    elif user_input == 'c':
        create(new_list, headers)
    elif user_input == 'r':
        retrieve(new_list, headers)
    elif user_input == 'u':
        update(new_list, headers)
    elif user_input == 'd':
        delete(new_list, headers)

file_output = []
file_output.append(headers)
for contact in new_list:
    file_output.append(list(contact.values()))
file_output = [",".join(line) for line in file_output]
file_output = "\n".join(file_output)

# Write to file
with open('contacts.csv', 'w') as file:
    file.write(file_output)

