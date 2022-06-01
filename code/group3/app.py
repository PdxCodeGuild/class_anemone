import re
from jsondb import JsonDB
db = JsonDB ('db.json')
db.load()

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        text = request.form['input_text']
        print(text)
        
    return

app.run(debug=True)