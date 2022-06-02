from flask import Flask, render_template, request, redirect
from modules import unit_converter


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    c_val = 0
    if request.method == 'POST':
        print(request.form)
        val_in = request.form['val_in']
        unit_in = request.form['unit_in']
        unit_out = request.form['unit_out']

        c_val = unit_converter(val_in,unit_in,unit_out)
        print(c_val)
    
    
    return render_template('index.html', c_val=c_val, unit_out=unit_out)

app.run(use_reloader=True, debug=True)