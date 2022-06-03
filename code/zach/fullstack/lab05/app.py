from flask import Flask, render_template, request, redirect
from modules import unit_converter


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    c_val = 0
    if request.method == 'POST':
        print(request.form)
        v_in = request.form['val_in']
        u_in = request.form['unit_in']
        u_out = request.form['unit_out']

        c_val, c_unit= unit_converter(v_in,u_in,u_out)
        print(c_val, c_unit)
    
    
    return render_template('index.html', c_val=c_val, c_unit=c_unit)

app.run(use_reloader=True, debug=True)