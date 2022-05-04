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

f = open('gettysburg_address.txt')
gba = f.read()
# print(gba)

words = [word for word in gba.split(' ')]
sentances = [word for word in gba.split('.')]
pass
# print(sentances,len(sentances)+1) # 10
# print(words,len(words)) # 238

char_plus_punct = "".join(words) 

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
def read(characters,words,sentances):
    ri = 4.71*(characters/words)+.5*(words/sentances)-21.43
    return round(ri)

read(c,w,s)
ri = read(c,w,s)
diff_read = 1 # access dictionary of dict_list 'ari_scale' that corresponds to the ari score, then access the value for the key 'grade_level'
ri_readout = ari_scale[ri]
r_level = ri_readout
print(f"""
The ARI for gettysburg-address.txt is {ari}
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.
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

"""