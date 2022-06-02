from flask import Flask, render_template, request, redirect
from Paw import Paw2
app = Flask(__name__)

paw = Paw2()

@app.route('/', methods =['GET', 'POST'])

def invoke():
    password = []
    if request.method == 'POST':
        # password.clear()
        password.append(paw.gen(request.form['letters'], request.form['numbers'], request.form['characters']))
        print(password)
        return redirect('/')
    return render_template('index.html', password=password)
    

app.run(debug=True)