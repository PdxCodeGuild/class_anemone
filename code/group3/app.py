from flask import Flask, render_template, request, redirect
import re
from jsondb import JsonDB
db = JsonDB('db.json')
db.load()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    todo = db.get('todo', 0)
    if request.method == 'POST':
        print(request.form)
        text = request.form['todo_text']
        priority = request.form['todo_priority']
        db_in = {text, priority}
    return render_template("index.html", todo=todo)


app.run(use_reloader=True, debug=True)
