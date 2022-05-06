'''ARI Lab''' # formula for reference
# 4.71 * (characters/word) + 0.5 * (words/sentences) - 21.43

'''First comment here was used as a test file open and close'''
# f = open('poem.txt')
# contents = f.read()
# print(contents)
# f.close()

'''Main program'''
# Count the number of sentences, words and characters
# store in variables and use in above equation
sentences = 0
words = 0
characters = 0

with open('poem.txt', 'r') as poem:
    for line in poem:
        all = line.split()
        sentences += line.count(".")
        words += len(all)
        characters += len(line)
# print(sentences, words, characters)

# Scale chart for reference
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


# Gather data from file and compare with chart
# 4.71 * (characters/word) + 0.5 * (words/sentences) - 21.43

data = 4.71 * (characters/words) + 0.5 * (words/sentences) - 21.43

# Loop through ari_scale to find the corresponding data
# round the data gathered above
for score in range(len(ari_scale)):
    gathered_data = ari_scale[round(data)]

# Display message containing all data
message = f'''
The ARI for the poem.txt is {round(data)}
This corresponds to a {gathered_data['grade_level']} difficulty level
that is suitable for an average person ages {gathered_data['ages']}
'''

print(message)
