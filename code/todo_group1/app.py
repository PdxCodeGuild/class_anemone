## import json contents
from jsondb import JsonDB
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

db = JsonDB('db.json')
db.load()


@app.route('/', methods=['GET', 'POST'])
def index():
    tasks = db.get('todos')
    if request.method == 'POST':
        contact_name = request.form['input_text']
        print(contact_name)
        # handle data here
        return redirect('/')
    return render_template('index.html',tasks = tasks)


