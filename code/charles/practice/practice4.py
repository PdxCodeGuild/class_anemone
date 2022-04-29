# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

from string import punctuation


def loud_text(text):
    x = "-".join(text.upper())
    return x

def test_loud_test():
    assert loud_text('hello') == 'H-E-L-L-O'
    assert loud_text('this is loud text') == 'T-H-I-S- -I-S- -L-O-U-D- -T-E-X-T'

print(test_loud_test)

# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    x = ''
    for char in word:
        x += char * 2
    return x

def test_double_letters():
    assert double_letters('hello') == 'hheelllloo'

print(test_double_letters())

# Count Letter
# Count the number of letter occurances in a string

def count_letter(letter, word):
    count = word.count(letter)
    return count

def test_count_letter():
    assert count_letter('i', 'antidisestablishmentterianism') == 5
    assert count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') == 2

print(test_count_letter)

# Latest Letter
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
  ...

def test_latest_letter():
    return latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') == 'v'


# Count Hi
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
  x = text.count('hi')
  return x

def test_count_hi():
    assert count_hi('hihi') == 2
    assert count_hi('hello hi llama hill') == 2


# Snake Case
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

def snake_case(text):
    x = text.lower().strip(f'{punctuation}')
    y = x.replace(' ', '_')
    return y

def test_snake_case():
    assert snake_case('Hello World!') ==  'hello_world'
    assert snake_case('This is another example.') == 'this_is_another_example'

# Camel Case
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

def camel_case(text):
    ...

def test_camel_case():
    assert camel_case('Hello World!') == 'helloWorld'
    assert camel_case('This is another example.') == 'thisIsAnotherExample'

## Alternating Case
# Write a function that converts text to alternating case.

def alternating_case(text):
    x = len(text)
    y = 2
    k = text.lower()
    p = text[k:x:y]
    return p

def test_alternating_case():
    assert alternating_case('Hello World!') ==  'HeLlO WoRlD!'
    assert alternating_case('This is another example.') == 'ThIs iS AnOtHeR ExAmPlE.'