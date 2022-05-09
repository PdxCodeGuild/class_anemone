

def list_split(fileName="contacts.csv"):
    with open(fileName) as file:
        column_names = file.readline() #reading the header line
        keys = column_names.split(",") #Splitting the line into keys
        number_of_columns = len(keys)

        list_of_dictionaries = []

        data = file.readlines()

        list_of_rows = []

        for row in data:
            list_of_rows.append(row.split(","))

        file.close()

        for item in list_of_rows:
            row_as_a_dictionary = {}
            for i in range(number_of_columns):
                row_as_a_dictionary[keys[i]] = item[i]
            list_of_dictionaries.append(row_as_a_dictionary)
            
        
        for i in range(len(list_of_dictionaries)):
            print(list_of_dictionaries)
            return list_of_dictionaries[i]

contact_list = [] #comprehension
list_split()




# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
#]