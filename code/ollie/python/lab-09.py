' Lab 9 - Ollie Callanan '

import re
import math

text = (open('gettysburg_address.txt')).read()
characters = re.findall(r"[a-zA-Z]", text)
words = text.split()
sentences = text.split('.')
sentences.pop()
num_chars = len(characters)
num_words = len(words)
num_sents = len(sentences)

ari_formula = math.floor(4.71 * (num_chars / num_words) + 0.5 * (num_words/num_sents) - 21.43)

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

print(f"""
The Gettysburg Address has an ARI score of {ari_formula}
making it suitable for students in {ari_scale[ari_formula]['grade_level']}
and people btween the ages {ari_scale[ari_formula]['ages']}.
""")