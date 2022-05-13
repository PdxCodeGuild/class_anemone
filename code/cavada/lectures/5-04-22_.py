"""character classes"""
# dav.d s
# david
# dav1d
# dav9d

"""match character ."""
# 
#
#
#

"""match digit \d"""
#
#
#
#

"""match white space \s"""
#
#
#
#

"""match word \w (letters, numbers, underscore)"""
#
#
#
#

"""character sets """
#
#
#
#

""""""
# my name is: [a-zA-Z]+
# My Name is: David 
#
#

"""repeats ? (<=1)"""
# ? 
#
#
#

"""repeats + (1+ times)"""
#
#
#
#

"""repeats {} (specific number: upper, lower) """
# leave out parameters 
#
#
#

"""repeats * (0+ times"""
#
#
#
#

"""\ escape escape characters"""
#
#
#
#

"""() capture groups"""
#
#
#
#

"""flags """
#
#
#
#

"""username + @ + domain name + . + TDL + TDL"""
#
#
# /\w+@([a-z0-9])+\.([a-z]{2,})/g
# 
import re

# """"""
# print(re.match('a', 'abcdef'))    # match
# print(re.match('c', 'abcdef'))    # no match
# print(re.search('c', 'abcdef'))   # match
# print(re.search('^c', 'abcdef'))  # no match
# print(re.search('^a', 'abcdef'))  # match
# result = re.match(r'\d{3}-\d{3}-\d{4}', '012-345-6789')
# print(result) # <re.Match object; span=(0, 12), match='012-345-6789'>
# #
# #
# #
# #

# """"""
# result = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
# print(result.group())      # The entire match 'Isaac Newton'
# print(result.group(1))     # The first parenthesized subgroup 'Isaac'
# print(result.group(2))     # The second parenthesized subgroup 'Newton'
# print(result.group(1, 2))  # Multiple arguments give us a tuple ('Isaac', 'Newton')

# result = re.match(r"([a-zA-Z]+) (\d+)", "June 14")
# print(result.start()) # the beginning of the match, 0
# print(result.end()) # the end of the match, 7
# print(result.group()) # same as result.group(0), 'June 14'
# print(result.group(1)) # 'June'
# print(result.group(2)) # '24'


#
#
#
#

"""re.split"""
s = "Hello! Is this a question? This is a statement."
# print(re.split('[ ]', s)) # ['Hello', ' Is this a question', ' This is a statement', '']
s_split = [s_split for s_split in s.split(' ')]#

#
#
#

"""f.read())"""


#
#
# f = open('filename.txt')  # open the file
# contents = f.read()  # read the contents
# print(contents)
# f.close()  # close the file

# try:
#     f = open('file.txt')
#     contents = f.read()
#     print(contents)
# except (IOError, OSError) as e:
#     print(e)
# finally:
#     f.close()

# with open('filename.txt', 'r') as f:
#     contents = f.read()



"""modes for calling open function"""
# default) r - open for reading
# w - open for writing
# x - open a file failing the file apready exits
# a - open for writing, appending if the file already exists
# t - read and write as text (default)
# b - read and write as binary

""""""
x=0
with open('file.txt', encoding='utf-8'):
    print(x)
#
#
#
#

""""""
""""""
#
#
#
#

""""""
#
#
#
#

""""""
#
#
#
#

""""""
#
#
#
#

""""""
#
#
#
#

""""""

x = []
list_a = [[x].append(input(f"{x}: ")) for x in range(10) ]
print(len(list_a),list_a,x)