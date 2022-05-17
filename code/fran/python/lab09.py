# Lab09 - Compute Automated Readability Index (ARI)
# Fran Kappes

# Import the regular expressions module
import re

# Create dictionary for the ARI scale
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

# Import text file that will contain a passage to be evaluated for an ARI score
file_name = 'gettysburg_address.txt'

with open(file_name, 'r') as f:
    contents = f.read()

#    print(contents)     ### TEST

# Count the number of characters in the passage
char_count_list = re.findall(r'[a-z,A-Z]', contents)
char_count = len(char_count_list)

#print(f"character count: {char_count}")     ### TEST


# Count the number of words in the passage
word_count_list = contents.split()
word_count = len(word_count_list)

#print(f"word count: {word_count}")      ### TEST


# Count the number of sentences in the passage
sentence_count_list = re.findall(r'[.?!]', contents)
sentence_count = len(sentence_count_list)

#print(f"sentence count: {sentence_count}")      ### TEST


# Calculate the ARI score
ari = round((4.71 * (char_count/word_count)) + (0.5 * (word_count/sentence_count)) - 21.43)

#print (f"ari: {ari}")       ### TEST

# Look up ARI grade and ARI age, based on the ARI score
ari_lookup = ari_scale[ari]
ari_grade = ari_lookup['grade_level']
ari_age = ari_lookup['ages']

#print(f"ari grade: {ari_grade}")    ### TEST
#print(f"ari age: {ari_age}")    ### TEST


# Report the score back to the user
print(f"""
--------------------------------------------------------
The ARI for {file_name} is {ari}
This corresponds to a {ari_grade} level of difficulty
that is suitable for an average person {ari_age} years old.
--------------------------------------------------------
""")