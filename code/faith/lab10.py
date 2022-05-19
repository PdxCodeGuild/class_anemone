with open('contacts.csv', 'r')as f:
    dcsv = f.read()


csv = dcsv.split("\n")
list= []
for line in csv:
    list.append(line.split(','))

keys = list[0]