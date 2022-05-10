"""setting csv file with variable to make as little specific to the file as possible"""
# csv = 'contacts.csv'
"""opening csv file while also splitting into disctict lines"""
# with open(csv, 'r') as f:
#     lines = f.read().split('\n')
# print(lines)
"""running a function that will essentially take the data and assemble a neat dictionary list"""
from re import X


csv = 'contacts.csv'

def open_file(csv):
    with open(csv,'rt') as f:
        lines = f.read().split('\n')
    # print(lines)
    return lines
lines = open_file(csv)    

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
    contacts = {}
    contact = {}
    contacts_list = []
    # print(cont_tuples)
    # contacts = []
    f1,f2=0,0
    for c in cont_tuples:
        f1+=1
        for key in keys:
            f2+=1
            # contact.update(c)
            # print("f2:",f2,"c:", c)
        contact.update(c)    
        # print("\n\tf1:",f1,"f2:",f2, contact)
        contacts.update(contact)
        if f1 == 3 and f2 == 9:
            print(f"contact1: {contact}")
            c1 = {}
            # c1.update = contact
            contacts_list.append(contact)
            
            print(contacts)
        elif f1 == 6 and f2 == 18:
            print(f"contact2: {contact}")
            c2 = []
            c
            contacts_list.append(c2)
            
            print(contacts)
        elif f1 == 9 and f2 == 27:
            print(f"contact3: {contact}")
            c3 = []
            # contact = c3
            contacts.append(c3)
            
            print(contacts)
        elif f1 == 12 and f2 == 36:
            print(f"contact4: {contact}")
            c4 = []
            # contact = c4
            contacts.append(c4)
            
            print(contacts)
        elif f1 == 15 and f2 == 45:
            print(f"contact5: {contact}, {type(contact)}")
            
    contacts.update(contact)

    # contacts.append(contact)
    # print(f1)    
    print(contacts)
    contacts_list.append(contacts)
    return contacts_list
    # contacts.append(contact)   
        
    # print(contacts)    
contacts=dict_list(lines)
print(contacts)

    # contacts.append(c1)
    # return contacts    
    # contacts.append(keys)
    # a = 0 # counter used for each for loop, ensures right value is selected when assigning dictionary key:value pairs
    # x = 0 # counter used throughout the 3 for loops to ensure that correct dictionary is being update,
    # for cont in conts:
    #     print(f"cont: {cont}")
        # contacts.append(cont)

    # print(contacts) [{'name': 'ronald parker', 'car': 'van', 'age': '53'},
    #                  {'name': 'elmo', 'car': 'bicycle', 'age': '12'}, 
    #                  {'name': 'sarah wilder', 'car': 'motorbike', 'age': '27'}]


    # return contacts # return of dictlist that can be futher maniuplated 
# lines=open_file(csv)
# contacts_list = csv_dict_rip(csv)
# print(dict_list(lines))
"""have my useable dictionary list data to maniupulate in python"""

"""other functions to use in CRUD """

def retrieve(contacts):
    x = 0
    a = 0
    user = input("Enter contact name: ")
    print(contacts) # [{'name': 'ronald parker', 'car': 'van', 'age': '53'}, {'name': 'elmo', 'car': 'bicycle', 'age': '12'}, {'name': 'sarah wilder', 'car': 'motorbike', 'age': '27'}]
    for contact in contacts:
        a +=1    
        # print(f"a: {a} contact key: {contact}") # {'name': 'ronald parker', 'car': 'van', 'age': '53'}
        for i in range(len(contact)): 
            x +=1
            # print(key) # name
            print(f"a: {a} contact value: {contact}")
            print(f"\tx: {x} contact: {contact[i]}")
            key = contact[i]

            # if a == 1 and x <4:
                # print(contact[key])
        

            # if user[key] == user:
            #     for key in contact:
            #         print(f"key: {key}")
            #         print(f"\t{key}: {contact[key]}")

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
    # user = input("See contact info: ")
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
    print(contacts)
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
            print('made it to the for loop')
            if choice == contact['name']:
                print(contact)
                contacts.remove(contact)   
                user = '' 
                break
    
    return contacts
# contacts_list = del_cont(contacts_list)
# print(contacts_list)

def dictlist_to_csv(contacts):
    line_u = []
    line1= []
    line2= []
    line3= []
    line4= []
    line5= []
    line6= []
    line7= []
    line8= []
    line9= []
    line10= []
    list_a = [contacts[x].values() for x in range(len(contacts))]
    tuples_u = []
    list_a = [tuples_u.append(list) for list in list_a]
    # print(tuples_u)
    x = 0
    for tuple_u in (tuples_u):
        line_bucket=[]
        for t in tuple_u:
            # print(t)
            if x < 3:
                line1.append(t)
            elif x < 6:
                line2.append(t)
            elif x < 9:
                line3.append(t)
            elif x < 12:
                line4.append(t)
            elif x < 15:
                line5.append(t)
            elif x < 18:
                line6.append(t)
            elif x < 21:
                line7.append(t)
            elif x < 24:
                line8.append(t)
            elif x < 27:
                line9.append(t)
            else:
                break
            x +=1   
    line_bucket.append(line1)
    line_bucket.append(line2)
    line_bucket.append(line3)
    line_bucket.append(line4)
    line_bucket.append(line4)
    line_bucket.append(line5)
    line_bucket.append(line6)
    line_bucket.append(line7)
    line_bucket.append(line8)
    line_bucket.append(line9)
    line_bucket.append(line10)
    for line in line_bucket:
        if line != '':
            line_u.append(line)  
    v = ['name', 'car', 'age']
    line_shell=[]
    line_shell.append(v)
    work = [line_shell.append(line) for line in line_u]
    # print(line_shell) # line_shell = [['ronald parker', 'buick', '50'], ['sarah wilder', 'tesla', '25'], ['huck jones', 'truck', '30']]
    """from here i will convert this set of tuples, 1 representing a set of variable for contact info, the rest represent variable values for each specific contact"""
    lines = []
    csv_data = []
    for line in line_shell:
        x=(','.join(line))
        lines.append(x)
    for line in lines:
        x = ('\n'.join(line))
        csv_data.append(x)
    if work == 'haha':
        print('popo')
    csv_data = ''
    lines = []
    for line in lines:
        x = (line+'\n')
        csv_data += x
    return csv_data
# ==================================================================================
def save_csv(csv_data):
    with open("contacts.csv", 'w') as f:
        f.write(csv_data)
    return print(f"csv file: {csv} saved with and changes")
# ==================================================================================

# lines=open_file(csv)
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
        while action in u and action != 'x':
            update(contacts)
            cont = input("update other contact data? ")
            if cont == 'n':
                action = 'x'
            contacts = (update(contacts))    
        while action in d and action != 'x':
            remove(contacts)    
            cont = input("delete other contact data? ")
            if cont == 'n':
                action = 'x'
            else:
                contacts = (remove(contacts))
        end = input('Select other option?: (y/n)')
        print(contacts)

        if end != 'y':
            save = 'save updates?'
            if save == 'y':
                csv_data = dictlist_to_csv(csv)    
                save_csv(csv_data)

            
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

# contacts = contacts_interface(lines)
# print("finding contacts")

# contacts = [{'name': 'ronald parker', 'car': 'van', 'age': '53'}, {'name': 'elmo', 'car': 'bicycle', 'age': '12'}, {'name': 'sarah wilder', 'car': 'motorbike', 'age': '27'}]
# print(contacts)
# for contact in contacts:
#     print(contact)
#     for c in contact:
#         print(c,contact[c])

""" CODE FOR RUNNING THE DICTLIST TO CSV and THEN CSV WRITE"""


# line_u = []
# line1= []
# line2= []
# line3= []
# line4= []
# line5= []
# line6= []
# line7= []
# line8= []
# line9= []
# line10= []
# list_a = [contacts[x].values() for x in range(len(contacts))]
# tuples_u = []
# list_a = [tuples_u.append(list) for list in list_a]
# # print(tuples_u)
# x = 0
# for tuple_u in (tuples_u):
#     line_bucket=[]
#     for t in tuple_u:
#         # print(t)
#         if x < 3:
#             line1.append(t)
#         elif x < 6:
#             line2.append(t)
#         elif x < 9:
#             line3.append(t)
#         elif x < 12:
#             line4.append(t)
#         elif x < 15:
#             line5.append(t)
#         elif x < 18:
#             line6.append(t)
#         elif x < 21:
#             line7.append(t)
#         elif x < 24:
#             line8.append(t)
#         elif x < 27:
#             line9.append(t)
#         else:
#             break
#         x +=1   
# line_bucket.append(line1)
# line_bucket.append(line2)
# line_bucket.append(line3)
# line_bucket.append(line4)
# line_bucket.append(line4)
# line_bucket.append(line5)
# line_bucket.append(line6)
# line_bucket.append(line7)
# line_bucket.append(line8)
# line_bucket.append(line9)
# line_bucket.append(line10)
# for line in line_bucket:
#     if len(line) == 3:
#         line_u.append(line)  
# print(f"line_u: {line_u}")        
# v = ['name', 'car', 'age']
# line_shell=[]
# line_shell.append(v)
# work = [line_shell.append(line) for line in line_u]
# # print(line_shell) # line_shell = [['ronald parker', 'buick', '50'], ['sarah wilder', 'tesla', '25'], ['huck jones', 'truck', '30']]
# """from here i will convert this set of tuples, 1 representing a set of variable for contact info, the rest represent variable values for each specific contact"""
# print(line_shell)
# csv_data = ''
# # print(lines)
# lines = []
# for line in line_shell:
#     x=(','.join(line))
#     lines.append(x)
# print(lines)
# a =0
# c=len(lines)
# print(c)
# for line in lines:
#     a +=1
#     if a <= c-1:
#         x = (line+'\n')
#         csv_data += x
#         # print(csv_data)
#     elif a == c:
#         csv_data += line
#         # print(csv_data)
    
    
# print(csv_data)

# save_csv(csv_data)
"""
checklist:
[] open csv file and convert strings into 'lines' (tuples)        - open_file(csv)
[] convert lines from csv rip into workable dictionary list       - dict_list(csv)  
[] create function to create user data                            - create(contacts)
[] create function to retrieve user data                          - retrieve(contacts)
[] create function to update user data                            - update(contacts)
[] create function to delete user data                            - delete(contacts)
[] create Contacts Interface 'while loop' including all funx      - contacts_interace(lines)
[x] create function to convert dictlist data to strings to write   - dictlist_to_csv(contacts)
[x] write update data to csv file                                  - save_csv(csv_data)   
    to csv file                                                                                    

"""