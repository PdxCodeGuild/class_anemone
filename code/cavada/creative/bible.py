import requests
import time
import json
import pprint
import sys

# """https://bible-api.com/john+3:16?callback=func"""
# url = 'https://bible-api.com/BOOK+CHAPTER:VERSE'
# response = requests.get(url)

old_ch = [50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4]
old_t = ['genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy', 'joshua', 'judges', 'ruth', '1 samuel', '2 samuel', '1 kings', '2 kings', '1 chronicles', '2 chronicles', 'ezra', 'nehemiah', 'esther', 'job', 'psalms', 'proverbs', 'ecclesiastes', 'song of solomon', 'isaiah', 'jeremiah', 'lamentations', 'ezekiel', 'daniel','hosea', 'joel', 'amos', 'obadiah', 'jonah', 'micah', 'nahum', 'habukkuk', 'zephaniah', 'haggai', 'zechariah', 'malachi']
# print(old_t, len(old_t),old_ch,len(old_ch))

new_ch = [28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]
new_t = ['matthew', 'mark', 'luke', 'john', 'acts', 'romans', '1 corinthians', '2 corinthians', 'galatians', 'ephesians', 'philippians', 'colossians', '1 thessalonians', '2 thessalonians', '1 timothy', '2 timothy', 'titus', 'philemon', 'hebrews', 'james', '1 peter', '2 peter', '1 john', '2 john', '3 john', 'jude', 'revelation']

""""""

old_test = {}
sys.stdout = open('old_testament.py', 'w')
for i, book in enumerate(old_t):
    url = f"https://bible-api.com/{book} 1-{old_ch[i]}"

    resp = requests.get(url)
    resp = resp.json()
    old_test.update({book:resp})
    time.sleep(.5) 
pprint.pprint(old_test)
sys.stdout.close()

new_test = {}
sys.stdout = open('new_testament.py', 'w')
for i, book in enumerate(new_t):
    url = f"https://bible-api.com/{book} 1-{new_ch[i]}"
    resp = requests.get(url)
    resp = resp.json()
    new_test.update({book:resp})
    time.sleep(.5) 
pprint.pprint(new_test)
sys.stdout.close()
