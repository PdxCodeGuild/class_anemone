with open('contacts.csv', 'r')as f:
    dcsv = f.read()


csv = dcsv.split("\n")
list= []
for line in csv:
    list.append(line.split(','))

key = list[0]
contacts = [dict(zip(key, values))for values in list[1::]]

def new_contacts(data, key):
    new_contacts = {}
    for x in key:
        new_contacts[key] = input(f'What is the new contacts {x}?')
    data.append(new_contacts) 
    