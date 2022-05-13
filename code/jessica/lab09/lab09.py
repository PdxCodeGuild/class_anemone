#Lab 09 ARI score
import math
import re
#opening the file and converting to a list
#file = open('example.txt', 'r')
# file_list = list(file)
# file_contents = file.read() 
# print(file_list) 

#dictionary for score values
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


with open('example.txt', 'r') as f:
    contents = f.read()

#Counting sentences
# print(type(file_list)) #<class 'list'>
sentences = int(contents.count("."))
#counting words
words = int(contents.count(' '))
#counting sentences
characters = re.findall(r'[a-zA-Z]', contents)
characters = len(characters)

print(sentences)
print(words)
print(characters)

ari_score = (4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43)

final_score = math.ceil(ari_score)

print(f"The ARI for gettysburg-address.txt is {final_score}")
print(f"This corresponds to a {ari_scale[final_score]['grade_level']} level of difficulty that is suitable for an average person {ari_scale[final_score]['ages']} years old.")
