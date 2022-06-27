csv = 'contacts.csv'
with open(csv, 'r') as f:
    csv_data = f.read()
    # print(f"csv_data: {csv_data}")
    lines = csv_data.split('\n')
# print(f"lines: {lines}")
# print(lines) # comma separated tuples
# lines = ['name,favorite color,favorite fruit', 'merritt,blue,apple', 'liz,yellow,mango', 'james,blue,strawberries']
tuples = [line.split(',') for line in lines]

# print(tuples) # each comma separate tuple is now a separate list 
# tuples = [['name', 'favorite color', 'favorite fruit'], ['merritt', 'blue', 'apple'], ['liz', 'yellow', 'mango'], ['james', 'blue', 'strawberries']]

keys = tuples[0] 
# print(keys)

tuples.pop(0)
contacts = []

# print(tuples)

# for tuple in tuples:
#     cdl = {}
#     for i in range(len(tuple)):
#         cdl[keys[i]] = tuple[i]
#     contacts.append(cdl)

# print(contacts)

# contacts = (list(zip(keys,tuple)))

# for i in range(len(tuples)):
#     contacts.append(dict(zip(keys,tuples[i])))

# print(contacts)

# for values in tuples:
#     contacts.append(dict(zip(keys,values)))

contacts = [dict(zip(keys,tuple)) for tuple in tuples]
# print(contacts)

def c(data,keys):
    data.append({key:(input(f'{key}? '))for key in keys})

def r(data, keys):
    choice=''
    key_s = '\n\t' + '\n\t'.join(keys)+ '\n' 
    x = 0
    method = keys[0]
    choice = input(f"{keys[0]}: ")
    while choice == 'other' and x == 0:
        method = input(f'Choose parameter to access contact: {key_s}  ')
        if method in keys:
            x +=1
        else:
            pass
        while choice == 'other' and not method in keys:
            print("incorrect parameter")
            exit = input("exit? ")
            if exit == 'y':
                choice = 'exit'
                break
            else:
                x = 0
                continue

    if choice == 'exit':
        pass      
    else:
        i = keys.index(method)
        x = 0
        print(choice, keys[i])
        keys[i]
        if choice == 'other':
            key = input(f'{keys[i]}: ')
            for contact in contacts:
                if key == contact[key]:
                    x +=1  
        else:
            key = keys[i]    
            for contact in contacts:
                if key == contact[key]:
                    x +=1            
            # else:
            #     key = keys[0]
            #     for contact in contacts:
            #         if key == contact[key]:
            #             x +=1
        # data_results = [contact for contact in data if contact[key_list] == contact_input]
        print('right before loop')
        for contact in data:
            
            for key in contact:
                print(f"\t{key}: {contact[key]}")
            break
        return contact
        
def u(data, keys):
    result = r(data, keys)
    key_s = '\n\t' + '\n\t'.join(keys)+ '\n' 
    choice = input(f"{keys[0]}, or 'other': ")
    if choice == 'other':
        key_u= input(f"key? {key_s}: ")
        value_u= input(f"value? ({key_u}): ")
        result[key_u]  =value_u
    else:
        key_u= keys[1]
        value_u= input(f"value? ({key_u}): ")
        result[key_u]  =value_u
        pass

def d(data, keys):
    result = r(data, keys)
    choice = input(f"{result} will be deleted, enter 'n' to cancel ")
    if choice != 'n':
        data.remove(result)
    else:
        pass



x = 0
while x == 0:
    # print(contacts)
    user = input("""
    (c)reate
    (r)ead
    (u)pdate
    (d)elete

    type 'quit'  """)
    if user.lower() in ['q','quit','exit', 'stop']:
        break

    elif user.lower() in ['c','create','add','new']:
        (c(contacts,keys))

    elif user.lower() in ['r', 'retrieve', 'view', 'read']:
        r(contacts,keys)

    elif user.lower() in ['u', 'update', 'change']:
        u(contacts,keys)

    elif user.lower() in ['d', 'delete', 'remove', 'trash']:
        d(contacts,keys)

    # else:
    #     print("you suck")
    #     break


tuples = []

lines = [keys]
for contact in contacts:
    line = []
    for key in keys:
        line.append(contact[key])
    lines.append(line)
print(lines)
csv_data = []

for line in lines:
    data = []
    for l in line:
        data = ','.join(line)
    csv_data.append(data)

# print(csv_data)    

csv_data = '\n'.join(csv_data)

def save(csv_data):
    
    with open("contacts.csv", 'w') as f:
        f.write(csv_data)
    return print(f"csv file: {csv} saved with and changes")

save(csv_data)