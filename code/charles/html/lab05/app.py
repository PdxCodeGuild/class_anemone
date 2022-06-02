from flask import Flask, render_template, request, redirect
from Paw import Paw2

app = Flask(__name__)

paw = Paw2()

@app.route('/', methods=['GET', 'POST'])

def invoke():
    # password = ""
    if request.method == 'POST':
        password = ""
        password += (paw.gen(int(request.form['letters']), int(request.form['numbers']), int(request.form['characters'])))
        return render_template('index.html', password=password)
    return render_template('index.html')
    

app.run(debug=True)