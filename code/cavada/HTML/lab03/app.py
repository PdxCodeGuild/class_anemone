import re
from flask import Flask, render_template, redirect, request
from jsondb import JsonDB


"""
import from jsondb import JsonDB
db = JsonDB('db.json')
db.load()
x = db.get('x', 0)
x += 1
db.set('x', x)
db.save()
"""

app = Flask(__name__)
db = JsonDB('db.json')
db.load()
import pprint
from creative.pyble import bible

book_options = bible.get_options()

print(book_options)

from creative.pyble import pyble

@app.route('/', methods=['GET', 'POST'])

def index():

    scripture = db.get('scripture')
    dict_list={}
    if request.method == 'POST':
        
        book = request.form['book']
        # index = book[1]
        print(f"book: {book}")
        book_strip = book.strip('()')
        # book_name = book[0]
        print(book_strip)
        book_info=book_strip.split(',')
        print(book_info)
        book_name=book_info[1].strip(" ' '")
        index = int(book_info[0])
        print(index,book_name)
        chapter = request.form['chapter']
        print(chapter)

        text= pyble[1][0]['new testament'][index][book_name.lower()][int(chapter)]
        print(text)
        dict_list = {'book': book_name, 'chapter': chapter, 'text':text}
        scripture.update(dict_list)
        db.set("scripture", scripture)
        db.save()

        return redirect ('/')
    elif request.method == 'GET':
        book = scripture['book']
        chapter = scripture['chapter']
        text = scripture['text']
        dict_list = {'book': book, 'chapter': chapter, 'text':text}

        return render_template("index.html",text=text, book_options=book_options, dict_list=dict_list)


app.run(debug=True)

