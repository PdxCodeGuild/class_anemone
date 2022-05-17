#ARI Score Lab-07

# import regular expressions
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


with open ('gettysburg.text', 'r') as f:
    contents = f.read()

def afi(contents):
    ##use find all expression / find all char
    characters = re.findall(r'[a-zA-Z0-9]',contents)
    all_chars = len(characters)

    ## find all words
    words = contents.split()
    all_words = len(words)

    ## find sentences wil splitting function
    sentences = re.findall('[.?!]',contents)
    all_sentences = len(sentences)

    #afi formula
    afi = 4.71 * (all_chars/all_words) + 0.5 * (all_words/all_sentences) - 21.43

    #Round up with round method
    total = round(afi)

    return (total)

score = afi(contents)
print(score)

print(f' The ARI for gettysburg.text is {score}. This corresponds to a {ari_scale[score]["grade_level"]} of difficulty that is suitable for an average person {ari_scale[score]["ages"]} years old ')




