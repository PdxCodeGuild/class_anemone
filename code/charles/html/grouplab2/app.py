'''
A simple JSON-based database that can be used with Flask.
Usage:
import from jsondb import JsonDB
db = JsonDB('database.json')
db.load()
x = db.get('x', 0)
x += 1
db.set('x', x)
db.save()
'''



from flask import Flask, render_template, request, redirect
import nosj

# load, save, __getitem__, __setitem__, __delitem__, get, set, clear,
# print(nosj.__getitem__("todos"))
js = nosj.JsonDB()
jsdb = js.load()
todos = js.__getitem__("todos")

x= js.get('x', 0)
print(x)

# for i, text in enumerate(todos):
#     for x in text:
#         print(x.value())

# print(js)
# print(jsdb)
# print(todos)

# app = Flask(__name__)

# @app.route('/')

# def index():
#     text = js.__getitem__('text')
#     return render_template('index.html', text=text)


# app.run(debug=True)