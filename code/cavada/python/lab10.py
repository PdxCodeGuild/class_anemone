"""setting csv file with variable to make as little specific to the file as possible"""
csv = 'contacts.csv'
option = 'r'

"""opening csv file while also splitting into disctict lines"""
with open(csv, option) as f:
    lines = f.read().split('\n')

"""running a function that will essentially take the data and assemble a neat dictionary list"""
def csv_dict_rip(lines):
    tuples = [] # this will be used for my 3 for loops that go into the tuples list and grab values for assigning the dictionary key-value pairs
    shell = [tuples.append((line.split(','))) for line in lines] # used 'shell' to pretty much do a list comprehension
    x = shell # threw shell into x so it doesn't mess with my function since it's going to be set to zero later
    cont1 = {} # dict shells set to assign and store contact info
    cont2 = {} 
    cont3 = {}  
    contacts_list= [] # dict list shell set to compile dictionaries as dict list
    contacts_list.append(cont1)
    contacts_list.append(cont2)
    contacts_list.append(cont3)
    a = 0 # counter used for each for loop, ensures right value is selected when assigning dictionary key:value pairs
    x = 0 # counter used throughout the 3 for loops to ensure that correct dictionary is being update,
    for key in tuples[0]: # first for loop used to collect and assign data to 1st contact that will be update in the 0th index of the contacts_list dict list dictionary for contact1 (ronald parker)
        dict_index = contacts_list[x] # used this to ensure nonspecificity in the key-value pair assignment in the next line by assigning the dictionary i need tp update for the next piece of code to a variable called 'dict_index' by assigning it to the xth dictionary in the dict list
        contact = tuples[x+1] # list_a index 1 (2nd) ['ronald', 'buick', '50'] # more nonspecificity by using the x+1 since i need to start accessing the contact data to assign values to contact keys
        dict_index[key]= contact[a] # assignment of key-value pair using ALL VARIABLES WOOOO!!!
        a += 1 # making sure my a value works for the duration of the for loop as i need it to target to next one over in the tuples each loop
    x += 1 # making sure my x variable is lined up for next for loop that will take care the (ne)xth dictionary
    # print(f"contact1: {cont1}") # print statement i used at some point for verification after a LOT of code being written and deleted
    a = 0 # reset a value to 0 in order to work again from left to right in list step-wise fashion 
    for key in tuples[0]: # same as above
        dict_index = contacts_list[x]
        contact = tuples[x+1]
        dict_index[key]= contact[a]   
        a += 1
    # print(f"contact2: {cont2}")
    x += 1
    a = 0
    for key in tuples[0]:
        dict_index = contacts_list[x]
        contact = tuples[x+1]
        dict_index[key]= contact[a]
        a += 1
    # print(f"contact3: {cont3}")
    x += 1 # cant remember if necessary, but not going to take out just yet
    contacts_list= [] # recompling of dict list
    # cont1 = cont1[0]
    contacts_list.append(cont1)
    contacts_list.append(cont2)
    contacts_list.append(cont3)
    return contacts_list # return of dictlist that can be futher maniuplated 
contacts_list = csv_dict_rip(lines)

print(contacts_list)

for contact in contacts_list: # print display of each contact entry
    print(contact)
