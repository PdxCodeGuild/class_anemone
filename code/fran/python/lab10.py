# Lab 10 - Contacts List
# Fran Kappes

# Open and read in contacts csv file
file_name = 'contacts_lab10.csv'

with open(file_name, 'r') as file:
    contents = file.read() 
    #print(contents)  ### TEST


# Create a string of individual contact dictionaries from the contacts file
contacts = []
lines = contents.split('\n')            # split record on new line character
header = lines[0].split(',')            # split header into individual items based on comma

for i in range(1,len(lines)):           # loop through all lines except the header
    row = lines[i].split(',')           # split record on comma
    contact = dict(zip(header,row))     # creates tuple
    #print(f"contact: {contact}")       # TEST
    contacts.append(contact)            # append individual's dictionary contents to contacts list



print(f"contacts list: {contacts}")