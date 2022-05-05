import math # to use math things
import re   # used to pull files from my PC to import into my code and then use to read it and edit it for the below re

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},       # taken from the lab example
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

with open('./gbadress.txt', 'r') as gbadress: #gettysburg adress (gbadress). I took i copied the letter and created a .txt file from a notepad and then saved it onto pc, then moved into folder
    contents = gbadress.read()     # used this from the lesson so it would automatic close and not waste ram and it isn't consantly double reading the file

letters = len(re.findall(r'[a-zA-Z0-9]', contents))   #using the len of contents and using the re.findall to then use r'[a-zA-Z0-9]' to find all letter and numbers and ext and give the amount back          
words = len(contents.split(' ')) # same as above but using the .split function to remove everything but the words and creating them into a list of all them selves and giving the amount back
sentences = len(re.split('[.]', contents)) # same as above but we are using the re.split function to edit the read file and create list up to [.] to seperate sentences and then give len back             
letters_words = letters/words # variable to divide letters and words because math is easy to mess up..
words_sent = words/sentences # same as above statement but for words and sentences
total = math.ceil(4.71*(letters_words) + 0.5*(words_sent) -21.43) # using the method givin on the lab lesson, then I used the import math function to use math.ceil() to round the numbers up to the nearest int
if total > 14:
    print(f'''The ARI for gettysburg-address.txt is {total}
    {ari_scale[14]['grade_level']} difficulty
    that is suitable for an average person {ari_scale[14]['ages']} years old!.''') # if total > then 14 it will always give the are scale key value of 14 college level
else:
    print(f'''
    The ARI for gettysburg-address.txt is {total}
    This corresponds to an {ari_scale[total]['grade_level']} difficulty
    that is suitable for an average person {ari_scale[total]['ages']} years old!.
    ''')

# copied the layout for how the lab should look at the end. I then used {total} to show the number givin back to determine reading range
# after i applaied {ariscale[total]} to let the dictionary know the key we are pulling from referenced by the number givin to us by total and then putting ['grade_level'] next to it to pull
# that value out from the key with out taking the entire key and applying it into the print().. sae goes for  {ari_scale[total]['ages']}