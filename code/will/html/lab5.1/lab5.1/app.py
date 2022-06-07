from flask import Flask, render_template, redirect, request
from jsondb import JsonDB
import string


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
    if request.method == 'POST':
        print(request.form)
        text = request.form['input_text']
        print(text)
        # do whatever with the text
        redirect('/')
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.whitespace
        output = ''
        for char in text:
            index = alphabet.find(char)
            if index == -1:
                output += char
        else:
                
                index %= len(alphabet)
                output += alphabet[index]
        return output
     
        return redirect('/')
    return render_template("index.html", to_do = to_do)



app.run(debug=True)