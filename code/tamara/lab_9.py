import re #import reg expression
import math #import math for rounding up

#dictionary for retrieving ages and grade_level by ari score
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

# open file and set contents to contents
with open('the_expanse_sample.txt', 'r') as the_expanse_sample:
    contents = the_expanse_sample.read()

# find word count by splitting at spaces and counting total of list
contents_words = contents.split(' ')
contents_words_count = len(contents_words)

# find sentance count by splitting at ?.! and gives length of list
# 1 is subtracted because there was an empty sentence '' for some reason
contents_sentances = re.split('[?.!]', contents) 
contents_sentances_count = len(contents_sentances) - 1

#find number of characters by putting them in list and taking length of list
contents_characters = re.findall(r'\w', contents)
contents_characters_count = len(contents_characters)

# find the ARI score and round it up
score = math.ceil(((contents_characters_count/contents_words_count)*4.71) + ((contents_words_count/contents_sentances_count)*.5) - 21.43)

# print the score output, grade level and age group
print(f"The ARI for the_expanse_sample.txt is {score}\nThis corresponds to an {ari_scale[score]['grade_level']} of difficulty\nThis is suitable for an average person aged {ari_scale[score]['ages']}")
