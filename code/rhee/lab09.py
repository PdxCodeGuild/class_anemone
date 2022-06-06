import re
# ARI scale
# open txt file with open('passage.txt', 'r')
# The score is computed by multiplying the number of characters divided by the number of words by 4.71, adding the
# number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a
# decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as
# scores of 14.

ari_scale = {
    1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages': '6-7', 'grade_level': '1st Grade'},
    3: {'ages': '7-8', 'grade_level': '2nd Grade'},
    4: {'ages': '8-9', 'grade_level': '3rd Grade'},
    5: {'ages': '9-10', 'grade_level': '4th Grade'},
    6: {'ages': '10-11', 'grade_level': '5th Grade'},
    7: {'ages': '11-12', 'grade_level': '6th Grade'},
    8: {'ages': '12-13', 'grade_level': '7th Grade'},
    9: {'ages': '13-14', 'grade_level': '8th Grade'},
    10: {'ages': '14-15', 'grade_level': '9th Grade'},
    11: {'ages': '15-16', 'grade_level': '10th Grade'},
    12: {'ages': '16-17', 'grade_level': '11th Grade'},
    13: {'ages': '17-18', 'grade_level': '12th Grade'},
    14: {'ages': '18-22', 'grade_level': 'College'}
}

with open("passage.txt", 'r') as passage:
    passage = passage.read()

list_sentences = re.split('[.?!]', passage)
list_words = passage.split(' ')
list_characters = re.findall(r'[A-Za-z0-9]', passage)

sentences = len(list_sentences)
words = len(list_words)
characters = len(list_characters)

# Do a word count
print("Shows how many words are present: ", words)
# # Do a character count
print("Shows how many characters are present: ", characters)
#  Do a sentence count
print("Shows how many sentences in file: ", sentences)

ari_score = round((4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43), 0)
print(f"Your ARI score is {ari_score}.")

print(f"The poem 'Do Not Go Gentle Into That Good Night' has an ARI score of {ari_score} making it suitable for "
      f"students in {ari_scale[ari_score]['grade_level']} and people between the ages {ari_scale[ari_score]['ages']}.")
