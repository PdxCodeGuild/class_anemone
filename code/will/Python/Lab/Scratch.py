contacts = []


def create():
    new_contact = input('Enter the name of the contact you would like to add')
    create_output = contacts.append(new_contact)
    return create_output
    
create()
print(contacts)