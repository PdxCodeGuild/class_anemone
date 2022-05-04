#Lab8
#Compute the ARI for a given body of text loaded in from a file.

import re

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


with open ('gettysburg-address.txt', 'r') as f:
    contents = f.read()

def AFI(contents):
    characters = re.findall(r'[a-zA-Z0-9]',contents)
    num_of_chars = len(characters)

    words = contents.split()
    num_of_words = len(words)

    sentences = re.findall('[.?!]',contents)
    num_of_sentences = len(sentences)

    AFI = 4.71 * (num_of_chars/num_of_words) + 0.5 * (num_of_words/num_of_sentences) - 21.43
    final_AFI = round(AFI)

    return (final_AFI)

gb_afi = AFI(contents)


print (f'The ARI for gettysburg-address.txt is {gb_afi} \nThis corresponds to a(n) {ari_scale[gb_afi]["grade_level"]} level of difficulty \nthat is suitable for an average person {ari_scale[gb_afi]["ages"]} years old.')

