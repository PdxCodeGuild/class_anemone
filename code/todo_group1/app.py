## import json contents
from jsondb import JsonDB
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

db = JsonDB('db.json')
db.load()

tasks = db.get('todos')
# print(tasks)      TEST

@app.route('/', methods=['GET', 'POST'])
def index():
    tasks = db.get('todos')
    if request.method == 'POST':
        task = request.form['input_text'], request.form['priority']
        print(task)
        
        # Add new task to task dictionary
        tasks.append(task)

        print(tasks)

        return redirect('/')
    return render_template('index.html',tasks=tasks)

app.run(debug=True)

