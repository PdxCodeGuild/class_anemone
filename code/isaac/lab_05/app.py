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
        encrypt = str.translate(cipher)
        encrypt = request.form['encrypt']
            
        return render_template('index.html', cipher=encrypt)
    return render_template('index.html')

app.run(debug=True)