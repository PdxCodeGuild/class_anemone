import re
list_of_list = []
contacts = []

#Importing the code snippets from the assignment
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    for line in lines:
        individual_items = line.split(',')
        list_of_list.append(individual_items)

#print(list_of_list)        

key = list_of_list.pop(0)
#Now that I have my list of lists I need to combine them to form their respective dictionary entries using the header with the other positions


for item in list_of_list:
    dict_1 = dict(zip(key, item))
    contacts.append(dict_1)
   
print(contacts)

def create():
    new_contact = input('Enter the name of the contact you would like to add')
    create_output = contacts.append(new_contact)
    return create_output
    

#def retrieve():
    reference = input('Enter the name of the contact whose information you want to retrieve ')


#def update():


#def delete():


#Here I am working on my REPL input command structure

def start_menu():
    print("Type c to Create a contact")
    print("Type r to Retrieve a contact")
    print("Type u to Update a contact")
    print("Type d to delete a contact")
   


    while True:
        user_input = input("What function would you like to perform?")
        if user_input.upper == "exit":
            break 

        elif user_input == 'help':
            start_menu()

    
        elif user_input == "d" :
            name_delete = input('Enter the name of the contact you want to delete')
            contacts.delete(name_delete)

        elif user_input == "u" :
            contact_update = input('Enter the name of the contact you want to update')


        elif user_input == "r" : 
            retrieve_name = input('Enter the name of the contact you want to retreive: ')
            contacts.read(retrieve_name)

        elif user_input == "c" :
            create_contact = input("Enter the name of the contact you would like to create")

