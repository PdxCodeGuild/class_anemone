"""setting csv file with variable to make as little specific to the file as possible"""
# csv = 'contacts.csv'
"""opening csv file while also splitting into disctict lines"""
# with open(csv, 'r') as f:
#     lines = f.read().split('\n')
# print(lines)
"""running a function that will essentially take the data and assemble a neat dictionary list"""
csv = 'contacts.csv'

def open_file(csv):
    with open(csv,'rt') as f:
        lines = f.read().split('\n')
    # print(lines)
    return lines
lines = open_file(csv)    
contact = []
contacts = []
contacts_list = []
# f1 = 0
# f2 = 0
def dict_list(lines):
    lines= open_file(csv)
    tuples=[]
    # print(f"lines:{lines}")
    shell = [tuples.append((line.split(','))) for line in lines] # used 'shell' to pretty much do a list comprehension
    # print(lines)
    x  = shell # threw shell into x so it doesn't mess with my function since it's going to be set to zero later
    # print(f"tuples: {tuples}")
    conts = [t for t in tuples]
    keys = conts.pop(0)
    x = -1
   # print(f"conts: {conts}")
    cont_tuples = []
    
    for cont in conts:
        x+=1
        for i, key in enumerate(keys):
            cont = {}
            # print(keys)
            contact = conts[x]
            # print(key, contact)
            cont[(key)] = contact[i]
            # print(c) # dict list shell set to compile dictionaries as dict lis.t
            cont_tuples.append(cont)
            # print(cont, contact)
            # for c in cont:
            #     cont[c]= contact[i]
            #     print(cont,c)
        # contact.append(cont)
        # print(cont)
    # print(f"cont_tuples: {cont_tuples}")
    # contacts = []
    f1 = 0
    f2 = 0
    contact = {}
    contacts = []
    contacts_list=[]
    c1 = {}
    c2 = {}
    c3 = {}
    c4 = {}
    c5 = {}
    # print(f1,f2)
    for c in cont_tuples:
        f1+=1
        # print(contacts)
        for key in keys:
            f2+=1
            # contact.update(c)
            # print("f2:",f2,"c:", c)
        contact.update(c)    
        # print("\n\tf1:",f1,"f2:"
        # ,f2, contact)
        # contacts.update(contact)
        
        if f1 == 3 and f2 == 9:
            # print(f"cont1: {contact}")
            c1.update(contact)
            # print(f"c1: {c1}")
            # c1.update = contact
            # contacts_list.append(contact)
            contacts_list.append(c1)
            
        elif f1 == 6 and f2 == 18:
            # print(f"cont2: {contact}")
            c2.update(contact)
            # print(f"c2:{c2}")
            contacts_list.append(c2)
            
            # print(contacts)
            # contacts_list.append(c2)
        elif f1 == 9 and f2 == 27:
            # print(f"cont3: {contact}")
            c3.update(contact)
            # print(f"c3:{c3}")
            contacts_list.append(c3)
            
            # print(contacts)
            # contacts_list.append(c3)
        elif f1 == 12 and f2 == 36:
            # print(f"cont4: {contact}")
            c4.update(contact)
            # print(f"c4:{c4}")
            contacts_list.append(c4)
            
            # print(contacts)
            # contacts_list.append(c4)
        elif f1 == 15 and f2 == 45:
            # print(f"cont5: {contact}")
            c5.update(contact)
            # print(f"c5:{c5}")
            
            # print(contacts)
            contacts_list.append(c5)

    return contacts_list

contacts=dict_list(lines)
# print(contacts)

"""have my useable dictionary list data to maniupulate in python"""

"""other functions to use in CRUD """

def retrieve(contacts):
    x = 0
    a = 0
    user = input("Enter contact name: ")
    for i, contact in enumerate(contacts):
        # print(contact)
        if user == contact['name']:
        # print(contact)
            for cont in contact:
                print(f"\t{cont}: {contact[cont]}")
            break

def create(contacts):  # function created to update contacts dict list with new dictionaries representing additional contacts
    user = ''
    while user != 'done' and user != 'n':
        user = input("Create Contact: (y/n) ")
        x = len(contacts)
        dict_name= ''
        if user == 'y' and user != 'done':
            name = input("name: ")
            car = input("car: ")
            age = input("age: ")
            dict_name = (dict_name+str(x+1))
            dict_name = {}
            dict_name['name'] = name
            dict_name['car'] = car
            dict_name['age'] = age
            contacts.append(dict_name)
            print(f"contact added: {contacts[x]}")
    return contacts
 
def update(contacts):
    choice = ''
    user = ''
    while user != 'done' and user != 'n' and choice != 'n':
        user = input("Update Contact: (y/n) ")
        if user == 'done' or user == 'n':
            break
        choice = input("Enter contact name: ")

        car = input("enter car: ")
        age = input("enter age: ")
        name = input("enter name: ('n' for no changes) ")
        # print(type(contacts_list),contacts_list)
        if choice != 'done' and choice != 'n' and choice != 'n':
            for contact in contacts:
                if choice == contact['name'] and choice != 'done' and choice != 'n':
                    print(f"{choice} profile updated...")
                    # print(contacts)
                    contact['car']=car
                    contact['age']=age
                    if name != 'n':
                        contact['name']=name

                    for c in contact:
                        print(f"\t{c}: {contact[c]}")
    # print(contacts)
    return contacts
# contacts_list = update_cont(contacts_list)
# print(contacts_list)

def remove(contacts):
    user = ''
    x = 0
    while user != 'done' and user != 'n':
        user = input("Remove Contact: (y/n) ")
        if user == 'n' or user == 'done':
            break
        choice = input("Enter contact name: ")
        for contact in contacts:
            # print(contact)
            # print('made it to the for loop')
            if choice == contact['name']:
                print(contact)
                contacts.remove(contact)   
                user = '' 
                break
    
    return contacts
# contacts_list = del_cont(contacts_list)
# print(contacts_list)

# ==================================================================================
def save_csv(csv_data):
    with open("contacts.csv", 'w') as f:
        f.write(csv_data)
    return print(f"csv file: {csv} saved with and changes")
# ==================================================================================

lines=open_file(csv)
def contacts_interface(lines):
    contacts = dict_list(lines)
    x = 0
    # print(contacts)
    print("welcome to interface")
    """code for contact list interface"""
    while x == 0:
        c = ['create', 'c']
        r = ['retrieve', 'r']
        u = ['update', 'u']
        d = ['delete', 'd']
        action = input("""
        Select option:
            -(c) Create:
            -(r) Retrieve:
            -(u) Update:
            -(d) Delete:
        """)
        cont = 'y'
        while action in r and action != 'x':
            cont = ''
            # print(contacts)
            retrieve(contacts)
            cont = input("retrieve other contact data? ")
            if cont == 'n':
                action = 'x'
        while action in c and action != 'x':
            create(contacts)
            # action = input("see another? ")  
            cont = input("create other contact data? ")
            if cont == 'n':
                action = 'x'
            else: 
                contacts = (create(contacts))
        while action in u and action != 'x':
            update(contacts)
            cont = input("update other contact data? ")
            if cont == 'n':
                action = 'x'
            else:
                contacts = (update(contacts))    
        while action in d and action != 'x':
            remove(contacts)    
            cont = input("delete other contact data? ")
            if cont == 'n':
                action = 'x'
            else:
                contacts = (remove(contacts))
        end = input('Select other option?: (y/n)')
        # print(contacts)

        if end != 'y':
        #     save = 'save updates?'
        #     if save == 'y':
        #         csv_data = dictlist_to_csv(csv)    
        #         save_csv(csv_data)

            
            break
    return contacts    
# ==================================================================================
"""call lines through interface funx if 'y' """

# interface = input("Start Contacts Interface: (y/n) ")
# if interface == 'y' and interface != 'n':
#     contacts_interface(lines)

# ==================================================================================
csv='contacts.csv'
# print(contacts(csv))
#=========================== write data to csv file ================================
csv = 'contacts.csv'

contacts = contacts_interface(lines)
# print("finding contacts")

# contacts = [{'name': 'ronald parker', 'car': 'van', 'age': '53'}, {'name': 'elmo', 'car': 'bicycle', 'age': '12'}, {'name': 'sarah wilder', 'car': 'motorbike', 'age': '27'}]
# print(contacts)
# for contact in contacts:
#     print(contact)
#     for c in contact:
#         print(c,contact[c])

""" CODE FOR RUNNING THE DICTLIST TO CSV and THEN CSV WRITE"""

# print(contacts)

# csv_data = dictlist_to_csv(contacts)

# print(csv_data)

"""I kinda gave up on working onthis, would have wanted to make the next code a function, but 
the following works well to format the updated dict list data to be called through my write
function to save the data to the existing csv file"""

list_a = [contacts[x].values() for x in range(len(contacts))]
# print(f"list_a: {list_a}")

lines= []
for list in list_a:
    values = []
    for l in list:
        # values = []
        values.append(l)
        # print(l) # prints dict values as strings
        # print(values)
    lines.append(values)  
    # print(shell) 

# print(lines)  
csv_data = 'name,car,age\n'
a =0
for line in lines:
    a+=1
    x = (','.join(line))
    #i for l in line:
    if a <= ((len(lines))-1):
        csv_data+=(x+'\n')
    else:
        # print("else worked")
        csv_data+=x
        
save_csv(csv_data)

"""
checklist:
[x] open csv file and convert strings into 'lines' (tuples)        - open_file(csv)
[x] convert lines from csv rip into workable dictionary list       - dict_list(csv)  
[x] create function to create user data                            - create(contacts)
[x] create function to retrieve user data                          - retrieve(contacts)
[x] create function to update user data                            - update(contacts)
[x] create function to delete user data                            - delete(contacts)
[x] create Contacts Interface 'while loop' including all funx      - contacts_interace(lines)
[x] create function to convert dictlist data to strings to write   - dictlist_to_csv(contacts)
[x] write update data to csv file                                  - save_csv(csv_data)   
    to csv file                                                                                    

"""