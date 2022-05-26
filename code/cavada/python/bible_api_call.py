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
old = {'genesis': 50, 'exodus': 40, 'leviticus': 27, 'numbers': 36, 'deuteronomy': 34, 'joshua': 24, 'judges': 21, 'ruth': 4, '1 samuel': 31, '2 samuel': 24, '1 kings': 22, '2 kings': 25, '1 chronicles': 29, '2 chronicles': 36, 'ezra': 10, 'nehemiah': 13, 'esther': 10, 'job': 42, 'psalms': 150, 'proverbs': 31, 'ecclesiastes': 12, 'song of solomon': 8, 'isaiah': 66, 'jeremiah': 52, 'lamentations': 5, 'ezekiel': 48, 'daniel': 12, 'hosea': 14, 'joel': 3, 'amos': 9, 'obadiah': 1, 'jonah': 4, 'micah': 7, 'nahum': 3, 'habukkuk': 3, 'zephaniah': 3, 'haggai': 2, 'zechariah': 14, 'malachi': 4}

new_ch = [28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]
new_t = ['matthew', 'mark', 'luke', 'john', 'acts', 'romans', '1 corinthians', '2 corinthians', 'galatians', 'ephesians', 'philippians', 'colossians', '1 thessalonians', '2 thessalonians', '1 timothy', '2 timothy', 'titus', 'philemon', 'hebrews', 'james', '1 peter', '2 peter', '1 john', '2 john', '3 john', 'jude', 'revelation']
new = {'matthew': 28, 'mark': 16, 'luke': 24, 'john': 21, 'acts': 28, 'romans': 16, '1 corinthians': 16, '2 corinthians': 13, 'galatians': 6, 'ephesians': 6, 'philippians': 4, 'colossians': 4, '1 thessalonians': 5, '2 thessalonians': 3, '1 timothy': 6, '2 timothy': 4, 'titus': 3, 'philemon': 1, 'hebrews': 13, 'james': 5, '1 peter': 5, '2 peter': 3, '1 john': 5, '2 john': 1, '3 john': 1, 'jude': 1, 'revelation': 22}
both = {'old testament': old, 'new testament': new}
both_ch = [old_ch, new_ch]
both_t = [old_t, new_t]
y = 0
""""""
entire_bible = {}
trip = True
books = {}
test = {}
entire_bible={}
a = -1
o_dict_list = []
n_dict_list = []
pyble = []
while trip == True and a < 1:
    a += 1
    
    for i, testament in enumerate(list(both.keys())):
        test= {}
        book_list = []
        for i, book in enumerate(both[testament]):  # genesis, exodus, deuteronomy....
            # print(book)
            x=0
            chapters = {}
            for i in range(both[testament][book]): # for the number of chapters in a given book
                # print(testament, book, i+1)
                chapter_verses = {}
                url = f"https://bible-api.com/{book} {i+1}"
                print(url)
                time.sleep(.0001) 
                
                resp = requests.get(url) 
                print(resp) 
                resp = resp.json()
                chap_verses_dict = resp['verses'] # verse_dict
                for dict in chap_verses_dict:
                    name = dict['book_name']
                    chap = dict['chapter'] #chapter number
                    verse = dict['verse'] #verse number
                    text = dict['text'] #verse text

                    chapter_verses.update({verse:text}) # adding verses to dictionary list shell
                chapters.update({chap:chapter_verses})  
            book_list.append({book:chapters})
        test.update({testament:book_list})
        pyble.append([test])   
    a+=1


sys.stdout = open('test.py','w', encoding= 'utf-8')   
pprint.pprint(pyble)
sys.stdout.close()    
    

skip = True
while skip == False:
    for i, pyb in enumerate(pyble):
        pyb = pyble[i]
        # print(testament)``
        for i, testmament in enumerate(pyb):
            testament = pyb[i]
            # pprint.pprint(testament)
            for i, book in enumerate(testament):
                book_list = testament[book]
                # pprint.pprint(book_list)
                for i, book in enumerate(book_list):
                    book = book_list[i]
                    print(book)


test_list = ['old testament','new testament']
old_ch = [50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4]
old_t = ['genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy', 'joshua', 'judges', 'ruth', '1 samuel', '2 samuel', '1 kings', '2 kings', '1 chronicles', '2 chronicles', 'ezra', 'nehemiah', 'esther', 'job', 'psalms', 'proverbs', 'ecclesiastes', 'song of solomon', 'isaiah', 'jeremiah', 'lamentations', 'ezekiel', 'daniel','hosea', 'joel', 'amos', 'obadiah', 'jonah', 'micah', 'nahum', 'habukkuk', 'zephaniah', 'haggai', 'zechariah', 'malachi']
old = {'genesis': 50, 'exodus': 40, 'leviticus': 27, 'numbers': 36, 'deuteronomy': 34, 'joshua': 24, 'judges': 21, 'ruth': 4, '1 samuel': 31, '2 samuel': 24, '1 kings': 22, '2 kings': 25, '1 chronicles': 29, '2 chronicles': 36, 'ezra': 10, 'nehemiah': 13, 'esther': 10, 'job': 42, 'psalms': 150, 'proverbs': 31, 'ecclesiastes': 12, 'song of solomon': 8, 'isaiah': 66, 'jeremiah': 52, 'lamentations': 5, 'ezekiel': 48, 'daniel': 12, 'hosea': 14, 'joel': 3, 'amos': 9, 'obadiah': 1, 'jonah': 4, 'micah': 7, 'nahum': 3, 'habukkuk': 3, 'zephaniah': 3, 'haggai': 2, 'zechariah': 14, 'malachi': 4}

new_ch = [28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]
new_t = ['matthew', 'mark', 'luke', 'john', 'acts', 'romans', '1 corinthians', '2 corinthians', 'galatians', 'ephesians', 'philippians', 'colossians', '1 thessalonians', '2 thessalonians', '1 timothy', '2 timothy', 'titus', 'philemon', 'hebrews', 'james', '1 peter', '2 peter', '1 john', '2 john', '3 john', 'jude', 'revelation']

new = {'matthew': 28, 'mark': 16, 'luke': 24, 'john': 21, 'acts': 28, 'romans': 16, '1 corinthians': 16, '2 corinthians': 13, 'galatians': 6, 'ephesians': 6, 'philippians': 4, 'colossians': 4, '1 thessalonians': 5, '2 thessalonians': 3, '1 timothy': 6, '2 timothy': 4, 'titus': 3, 'philemon': 1, 'hebrews': 13, 'james': 5, '1 peter': 5, '2 peter': 3, '1 john': 5, '2 john': 1, '3 john': 1, 'jude': 1, 'revelation': 22}
both = {'new testament':new,'old testament':old}


trip = False

while trip == True:
    for i, testament in enumerate(test_list):
        print(f"{i+1}) {testament}")
    test_num = int(input('test: '))-1
    test = test_list[test_num]
    testament = pyble[test]
    # print(test)

    if test == 'new testament':
        ref_book = new_t
        ref_chap = new_ch

    else:
        ref_book = old_t
        ref_chap = old_ch

    for i, book in enumerate(ref_book):
        print(f"{i+1}) {book} ")

    book_num = int(input('book: '))-1
    bk = ref_book[book_num]
    book = testament[bk]

    chapter_choice = input(f"pick chapter: 1-{ref_chap[book_num]} \nor press enter to start from the 1st chapter\n")
    selection = []
    if chapter_choice == '':
        section = []
        for chapter in book:
            sub_section = []
            chapter = book[chapter]
            # print(chapter)

            for verse in chapter:
                verse = chapter[verse]
                v = verse.strip('\n')
                # print(v)
                # time.sleep(.5)
                sub_section.append(v)
            section.append(sub_section)
            

        selection.append(section) 
        for section in selection:
                for i, sub_section in enumerate(section):
                    print('\tchapter:',i+1, '\n')
                    for i, sub in enumerate(sub_section):
                        print(i+1, sub)   
    elif int(chapter_choice) in range(ref_chap[book_num]):
        chapter = book[int(chapter_choice)]
        print(chapter)
        break
        for i, verse in enumerate(chapter):
            verse = chapter[verse]
            v = verse.strip('\n')
            selection.append(v)
        # print(selection)
        print('\tchapter:',i+1, '\n')
        for i, section in enumerate(selection):
            print(i+1, section)
