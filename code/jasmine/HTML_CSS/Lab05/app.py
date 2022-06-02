
from flask import Flask, render_template, request, redirect


app = Flask(__name__)

unit_convert = {
    'meters': 1,
    'feet': 0.3048,
    'miles': 1609.34,
    'kilometers': 1000,
    'inches': 0.0254,
    'yard': 0.9144


}

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'GET':
    #     return render_template('index.html')
    if request.method == 'POST':
        distance_amount = request.form['distance_amount']
        distance_amount = float(distance_amount)
        meters = unit_convert(distance_amount)
        return render_template('index.html', meters=meters)
    else:
        return render_template('index.html', meters='')


app.run(debug=True)
