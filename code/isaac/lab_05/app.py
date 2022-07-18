import re
import string
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        alpha = 'abcdefghijklmnopqrstuvwxyz' 
        bravo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
        cipher = str.maketrans(alpha + bravo, alpha[13:] + alpha[:13] + bravo[13:] + bravo[:13])
        encode = request.form['encode']
        encrypt = str.translate(encode, cipher)
            
        return render_template('index.html', cipher=encrypt)
    return render_template('index.html')

app.run(debug=True)