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

def dict_list(lines):
    lines= open_file(csv)
    tuples=[]
    print(f"lines:{lines}")
    # tuples = [['name,car,age', 'ronald parker,van,53', 'elmo,bicycle,12', 'sarah wilder,motorbike,27', 'harry carey,limo,45', 'harry carey,limo,45', 'moe skaggs,scooter,32', 'dwayne forthwright,pickup,82', 'chicken little,coupe,9', 'jiminy cricket,shoe,28']] # this will be used for my 3 for loops that go into the tuples list and grab values for assigning the dictionary key-value pairs
    shell = [tuples.append((line.split(','))) for line in lines] # used 'shell' to pretty much do a list comprehension
    # print(lines)
    x  = shell # threw shell into x so it doesn't mess with my function since it's going to be set to zero later
    cont1 = {} # dict shells set to assign and store contact info
    cont2 = {} 
    cont3 = {} 
    cont4 = {}
    cont5 = {}
    cont6 = {}
    cont7 = {} 
    cont8 = {}
    cont9 = {}
    cont10 = {}
    cont_basket= []
    cont_basket.append(cont1)
    cont_basket.append(cont2)
    cont_basket.append(cont3)
    cont_basket.append(cont4)
    cont_basket.append(cont5)
    cont_basket.append(cont6)
    cont_basket.append(cont7)
    cont_basket.append(cont8)
    cont_basket.append(cont9)
    # print(lines)
    # print(tuples)
    # tuples = [x for x in tuples if x != ['']]
    print(f"tuples: {tuples}")
    conts = [t for t in tuples]
    v = conts.pop(0)
    print(f"conts: {conts}")
    contacts= [] # dict list shell set to compile dictionaries as dict list
    a = 0 # counter used for each for loop, ensures right value is selected when assigning dictionary key:value pairs
    x = 0 # counter used throughout the 3 for loops to ensure that correct dictionary is being update,
    for cont in conts:
        print(cont)
        for key in v: # first for loop used to collect and assign data to 1st contact that will be update in the 0th index of the contacts_list dict list dictionary for contact1 (ronald parker)
            print(key)
            dict_index = cont_basket[x] 
            contact = conts[x+1] 
            dict_index[key]= contact[a] 
            a +=1 
            x +=1 
    # # print(f"contact1: {cont1}") # print statement i used at some point for verification after a LOT of code being written and deleted
    # a = 0 # reset a value to 0 in order to work again from left to right in list step-wise fashion 
    # for key in tuples[0]: # same as above
    #     dict_index = cont_basket[x]
    #     contact = tuples[x+1]
    #     dict_index[key]= contact[a]   
    #     a += 1
    # # print(f"contact2: {cont2}")
    # x += 1
    # a = 0
    # for key in tuples[0]:
    #     dict_index = cont_basket[x]
    #     contact = tuples[x+1]
    #     dict_index[key]= contact[a]
    #     a += 1
    # # print(f"contact3: {cont3}")
    # x += 1 # cant remember if necessary, but not going to take out just yet
    contacts= [] # recompling of dict list
    # cont1 = cont1[0]
    # print(cont_basket)
    for cont in cont_basket:
        if cont != {} and type(cont) != list:
            contacts.append(cont)
    print(f"contacts:{contacts}")

    return contacts # return of dictlist that can be futher maniuplated 
# lines=open_file(csv)
# contacts_list = csv_dict_rip(csv)

"""have my useable dictionary list data to maniupulate in python"""

"""other functions to use in CRUD """

def retrieve(contacts):
    user = input("Enter contact name: ")
    # print(contacts) # [{'name': 'ronald parker', 'car': 'van', 'age': '53'}, {'name': 'elmo', 'car': 'bicycle', 'age': '12'}, {'name': 'sarah wilder', 'car': 'motorbike', 'age': '27'}]
    for contact in contacts:
        # print(contact) # {'name': 'ronald parker', 'car': 'van', 'age': '53'}
        for key in contact: 
            # print(key) # name
            if contact[key] == user:
                for key in contact:
                    print(f"\t{key}: {contact[key]}")
                # print(f"info: {contact}")
                # p
                # rint(f"contacts list: {contacts}")
            # else:
                # print("contact not found")

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
    print(contacts)
    print("welcome to interface", contacts)
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

contacts = contacts_interface(lines)
# print("finding contacts")

# contacts = [{'name': 'ronald parker', 'car': 'van', 'age': '53'}, {'name': 'elmo', 'car': 'bicycle', 'age': '12'}, {'name': 'sarah wilder', 'car': 'motorbike', 'age': '27'}]
# print(contacts)
# for contact in contacts:
#     print(contact)
#     for c in contact:
#         print(c,contact[c])

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
    if len(line) == 3:
        line_u.append(line)  
print(f"line_u: {line_u}")        
v = ['name', 'car', 'age']
line_shell=[]
line_shell.append(v)
work = [line_shell.append(line) for line in line_u]
# print(line_shell) # line_shell = [['ronald parker', 'buick', '50'], ['sarah wilder', 'tesla', '25'], ['huck jones', 'truck', '30']]
"""from here i will convert this set of tuples, 1 representing a set of variable for contact info, the rest represent variable values for each specific contact"""
print(line_shell)
csv_data = ''
# print(lines)
lines = []
for line in line_shell:
    x=(','.join(line))
    lines.append(x)
print(lines)
a =0
c=len(lines)
print(c)
for line in lines:
    a +=1
    if a <= c-1:
        x = (line+'\n')
        csv_data += x
        # print(csv_data)
    elif a == c:
        csv_data += line
        # print(csv_data)
    
    
print(csv_data)

save_csv(csv_data)
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