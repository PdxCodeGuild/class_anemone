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




#Here I am working on my REPL input command structure

def start_menu():
    print("Type c to Create a contact")
    print("Type r to Retrieve a contact")
    print("Type u to Update a contact")
    print("Type d to delete a contact")
    print("Type s to Save your contacts for export")
    print("Type o to open a contact")
    print("Type 'Help' to see this lsit again")
    print("Type 'Exit' to exit program")


    while True:
        user_input = input("What function would you like to perform?")
        if user_input.upper == "exit":
            break 

        elif user_input == 'help':
            start_menu()

        elif user_input == 'o':
            file_select = input('Enter the filepath you want to access')
            contacts.load(file_select)
        
        elif user_input == "s" :
            contacts.save(file_select)

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

start_menu()