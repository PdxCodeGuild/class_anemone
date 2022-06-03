import json


class C_List:
    def __init__(self):
        self.contacts = []

    # create contact information
    def load(self):
        with open("contacts.json", "r") as f:
            contacts_content = f.read()
            contacts_dict = json.loads(contacts_content)
        self.contacts = contacts_dict["contacts"]

    def count(self):
        return len(self.contacts)

    # saving contact information
    def save(self):
        with open("contacts.json", "w") as f:
            saved_contacts_dict = {"contacts": self.contacts}
            f.write(json.dumps(saved_contacts_dict, indent=2))

    # showing information for contacts
    def print(self):
        for i in range(len(self.contacts)):
            # print(self.contacts[i])
            print(f"First name: {self.contacts[i]['First Name']}")
            print(f"Last name: {self.contacts[i]['Last Name']}")
            print(f"Address: {self.contacts[i]['Address']}")
            print(f"Phone #: {self.contacts[i]['Phone_number']}")
            print("                                           \n")

    # removing contact information from list
    def delete(self, f_name, l_name):
        for contact in self.contacts:
            if f_name.lower() == contact["Frst name"] and l_name.lower() == contact["Last name"].lower():
                self.contacts.remove(contact)
        print(f">>> {contact['First Name'] + ['Last Name']} has been removed\n")

    # update contact information
    def update(self, new_f_name, new_l_name, address, new_phone_number):
        for contact in self.contacts:
            if f_name.lower() == contact["First name"].lower():
                self.contacts.remove(contact)
            if l_name.lower() == contact["Last name"].lower():
                new_dict = {"First name": new_f_name, "Last name": new_l_name, "Address": address, "Phone_number": new_phone_number}
                self.contacts.append(new_dict)
        print(f">>> {contact['First Name'] + {contact['Last Name'} has been updated\n")


contact_list = ContactList()
contact_list.load()
while True:
    print("Commands to be entered: create, read, delete, update, exit, or help")
    command = input("Enter a command: ")
    if command == "create":
        print("Please enter contact information:")
        f_name = input("Enter First name: ")
        l_name = input("Enter Last name: ")
        address = input("Enter Address: ")
        phone_number = input("Enter phone number: ")
        contact_list.load()
        print(f"You have a total of {contact_list.count()} contacts.")

    elif command == "read":
        contact_list.print()

    elif command == "delete":
        f_name = input("Enter first name to remove: ")
        l_name = input("Enter last name to remove:")
        contact_list.delete(f_name, l_name, address, Phone_number)

    elif command == "update":
        print("Enter info of contact to add:")
        previous_f_name = input("Enter First name to update: ")
        previous_l_name = input("Enter Last name to update: ")
        new_f_name = input("Enter First name: ")
        new_l_name = input("Enter Last name:")
        add_phone_number = input("Enter Phone Number: ")
        add_address = input("Enter address: ")
        contact_list.update(previous_f_name, previous_l_name, new_f_name, new_l_name, add_phone_number, add_address)

    elif command == "help":
        print("Available commands:")
        print("create   - create contacts to file")
        print("read     - read contacts from file")
        print("delete   - delete contact")
        print("update   - update contact")
        print("exit     - leave the program")
    elif command == "exit":
        break
    else:
        print("Key not permitted, try again!")
