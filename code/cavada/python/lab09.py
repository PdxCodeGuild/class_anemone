# scale pulled from lab info
ari_scale = { 
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
# opening random text file i found on internet that had 235 word ct
with open('gettysburg_address.txt','r') as f: # ensures that the file is closed 
    gba = f.read() # assigns text as string i can use as a variable
# print(gba)

words = [word for word in gba.split(' ')] # create list to count length of it to determine word ct
sentances = [word for word in gba.split('.')] # create list to count length of it to determine sentance ct
pass
# print(sentances,len(sentances)+1) # 10
# print(words,len(words)) # 238

char_plus_punct = "".join(words) # did this to get rid of punctuation other than period(only included commas, so I only filtered with commas in mind)

# print(char_plus_punct, len(char_plus_punct)) # 1038 characters, including all punctuation
# for character in char_plus_punct:
char_plus_period = []
character = [char for char in char_plus_punct if not char == "," and not char == "."] 
# print(len(character)) # 1007 characters 
# char_list = [char_list.append[character] for character in gba]
# print(characters)
# words = []
# characters = 
# c = len(characters)

# list_a = [[x].append(input(f"{x}: ")) for x in range(10) ]
# print(len(list_a),list_a,x)
# rating = 
c = len(character)
w = len(words)
s = len(sentances)
# print(c,w,s)
def read(characters,words,sentances): # function to calc readibility index
    ri = 4.71*(characters/words)+.5*(words/sentances)-21.43
    return round(ri) # return rounded result

read(c,w,s)
ari = read(c,w,s) # assign this to variable to make it easier to use
# access dictionary of dict_list 'ari_scale' that corresponds to the ari score, then access the value for the key 'grade_level'
ri_dict_list = ari_scale[ari] # accessing dictionary from dictionary list 'ari_scale'
grade_level = ri_dict_list['grade_level'] # accessing value using corresponding key
ages = ri_dict_list['ages'] #  accessing value using corresponding key

print(f"""
Text: {gba} 

The ARI for gettysburg-address.txt is {ari}
This corresponds to a {grade_level} level of difficulty
that is suitable for an average person {ages} years old.
""")


# Score  Ages     Grade Level
#      1       5-6    Kindergarten
#      2       6-7    First Grade
#      3       7-8    Second Grade
#      4       8-9    Third Grade
#      5      9-10    Fourth Grade
#      6     10-11    Fifth Grade
#      7     11-12    Sixth Grade
#      8     12-13    Seventh Grade
#      9     13-14    Eighth Grade
#     10     14-15    Ninth Grade
#     11     15-16    Tenth Grade
#     12     16-17    Eleventh grade
#     13     17-18    Twelfth grade
#     14     18-22    College
""" """
#
#
#
#

""""""
#
#
#
#

""""""
#
#
#
#

""""""
#
#
#
#

