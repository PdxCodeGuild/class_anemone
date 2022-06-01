from jsondb import JsonDB
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

db = JsonDB("db.json")
db.load()


@app.route('/', methods=['GET', 'POST'])

def index():
    todos = db.get("todos")
    if request.method == 'POST':
        return redirect('/')
    return render_template('index.html',todos=todos)


@app.route('/cat/')

def house():
    pass

app.run(debug=True)