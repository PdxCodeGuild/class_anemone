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
        print('request.form;',request.form)
        text = request.form['input_text']
        print('test text',text)
        # do whatever with the text
        #redirect('/')
 
        Dictionary = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', }
        result = ''
        for char in text:
            if char in Dictionary.keys():
                result += Dictionary[char]
        
        output = result
       
        return render_template('index.html',output=output)
     
       # return redirect('/')
    return render_template("index.html")



app.run(debug=True)