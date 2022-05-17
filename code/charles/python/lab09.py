
from fileinput import filename
import re
import math


address = open('gettysburg_address.txt')                                    # opening and reading the designated text file
contents = address.read()                                                   # the text file I found has a bunch of -- on the finale line and get conveted to their own strings...

characters = len(re.findall(r'\w', contents))                               # \w+ return my ari as -4...
words = len(contents.split())
sentences = len(re.split('[.]', contents)) - 1                              # I could not for the life of me find out why it was giving me 11 sentences instead of 10... 
ari = math.ceil(4.71*(characters/words) + 0.5*(words/sentences) -21.43)     # the last . was getting put as its own string so i subtrated 1, becasue popping it made it a 0
                                                                            # math.ceil to round up to the higher integer
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

print(f'''The ARI for {address.name} is {ari}. 
This corresponds to {ari_scale[ari]['grade_level']} of difficulty. 
That is suitable for an average person of {ari_scale[ari]['ages']}''')  # was just saying yesterday that i could figure out how a list within a list work... but now im thinking its similar to dictionaries