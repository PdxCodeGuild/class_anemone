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

@app.route('/', methods=['GET', 'POST'])

def index():
    to_do = db.get('todos')
    return render_template("index.html", to_do = to_do)

app.run(debug=True)

