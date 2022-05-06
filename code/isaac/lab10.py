'''Contact List'''

# Open and read the csv file 'contacts.csv'
from requests import head


with open('contacts.csv', 'r') as file:
    lines = file.read().split("\n")
    # print(lines)


# Create a list containing contacts
contact_list = []
for line in lines:
    contact_list.append(line.split(","))
# print(contact_list)
headers = contact_list.pop(0)
# print(headers, contact_list)


new_list = []
for contact in contact_list:
    contact_dict = {headers[0]: contact[0], headers[1]: contact[1], headers[2]: contact[2]}
    new_list.append(contact_dict)
# print(new_list)

# Create new contact
def create(new_list, headers):
    user_name = input("What is your contacts name? ")
    user_fruit = input("What is their favorite fruit? ")
    user_color = input("What is their favorite color? ")
    new_dict = {headers[0]: user_name, headers[1]: user_fruit, headers[2]: user_color}
    new_list.append(new_dict)
    return new_list

# Retrieve contact
def retrieve(new_list):
    user_retrieve = input("Who are you looking for? ")
    if user_retrieve in new_list:
        con_ret = headers[0]
        return con_ret
print(retrieve(new_list))
        