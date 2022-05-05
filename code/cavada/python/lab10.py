with open("contacts.csv", "r") as f:
    lines = f.read().split('\n')

tuples = []
set = [tuples.append((line.split(','))) for line in lines]

cont1 = {}
cont2 = {}
cont3 = {}    
contacts_list= []
contacts_list.append(cont1)
contacts_list.append(cont2)
contacts_list.append(cont3)

a = 0
x = 0
shell = []
for l in tuples:
    for key in tuples[0]:
        dict_index = contacts_list[x]
        contact = tuples[1] # list_a index 1 (2nd) ['ronald', 'buick', '50']
        # print(contact[a])
        cont1[key]= (contact[a])
        a += 1
    x += 1
    print(f"contact1: {cont1}")
    a = 0
    for key in tuples[0]:
        dict_index = contacts_list[x]
        cont2[key]= (contact[a])    
        a += 1
    print(f"contact2: {cont2}")
    x += 1
    a = 0
    for key in tuples[0]:
        index = contacts_list[x]
        cont3[key]= (contact[a])
        a += 1
    print(f"contact3: {cont3}")
    x += 1
    break

print(contacts_list)
contacts_list= []
contacts_list.append(cont1)
contacts_list.append(cont2)
contacts_list.append(cont3)

# print(cont1)
# print(cont2)
# print(cont3)
for contact in contacts_list:
    print(contact)
"""
for key in list_a[0]:
    x = 1
    contact = list_a[x] # list_a index 1 (2nd) ['ronald', 'buick', '50']
    for i, dict in enumerate(contacts_list):
        dict[key]= contact[b] # make dictionary entry with key from for loop and value at list index
        contacts_list.append(dict)
        b += 1
        a += 1
        print(dict)
"""
# print(contacts_list)            

contacts_list = [{'name': 'ronald parker', 'car': 'buick', 'age': '50'}, {'name': 'sarah wilder', 'car': 'tesla', 'age': '25'}, {'name': 'huck jones', 'car': 'truck', 'age': '30'}] 