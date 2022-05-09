'''Contact List'''

# Open and read the csv file 'contacts.csv'
with open('contacts.csv', 'r') as file:
    contact_list = file.read().split("\n")
    # print(lines)
    
# Create a list containing contacts
contact_list = [line.split(",") for line in contact_list.split("\n")]

headers = contact_list[0]

# Make a list of contacts to search for through the csv file
# use the zip() function for familiarity purposes
new_list = [dict(zip(headers, values)) for values in contact_list[1::]]

# Create new conact function
# add a new contact by name, favorite fruit and favorite color
def create(new_list, headers):
    new_list.append({header: input(f"What is your contacts {header}?  ") for header in headers})
    return new_list

# Create a retrieve contact name function.
# Use headers as search options for contact
def retrieve(new_list, headers):
    header_search = "\n" + "\n".join(headers) + "\n"
    contact_search = input(f"What would you like to search for today?  Options are: \n{header_search.title()}\n")
    search_input = input(f"Enter {contact_search}: ")

    search_results = list(filter(lambda contact: contact[contact_search] == search_input, new_list))
    return search_results

# Update the contacts name, fruit or color
def update(new_list, headers):
    search_results = retrieve(new_list, headers)
    # update a specific index of the contact
    positon_update = int(input(f"Which contact would you like to edit? (1-{len(search_results)})")) -1
    list_update = input()