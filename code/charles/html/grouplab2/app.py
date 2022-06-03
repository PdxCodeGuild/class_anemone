from jsondb import JsonDB
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

db = JsonDB("db.json")
db.load()


@app.route('/', methods=['GET', 'POST'])

def index():
    todos = db.get("todos")
    if request.method == 'POST':
        todo = {'text': request.form['todo item'], 'priority': request.form['priority']}
        todos.append(todo)
        db.save()
        return redirect('/')
    return render_template('index.html',todos=todos)

app.run(debug=True)