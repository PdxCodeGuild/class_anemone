
from flask import Flask, render_template, request


app = Flask(__name__)

# unit_convert = {
#     'meters': 1,
#     'feet': 0.3048,
#     'miles': 1609.34,
#     'kilometers': 1000,
#     'inches': 0.0254,
#     'yard': 0.9144


# }

@app.route('/', methods=['GET', 'POST'])
def index():
            
    unit_convert = {
        'meters': 1,
        'feet': 0.3048,
        'miles': 1609.34,
        'kilometers': 1000,
        'inches': 0.0254,
        'yard': 0.9144


    }

    if request.method == 'GET':
        print("GET working")
        return render_template('index.html')


    elif request.method == 'POST':
        print("Hello")
        distance_amount = request.form['distance_amount']
        distance_amount = float(distance_amount)
        print(distance_amount)
        old_units = request.form['input_units']
        new_units = request.form['output_units']
        meters_convert = distance_amount * unit_convert[old_units]
        # meters_convert = float(meters_convert)
        new_convert = round(meters_convert / unit_convert[new_units], 3)
        return render_template('index.html', distance_amount=distance_amount, old_units=old_units,new_units=new_units, result=new_convert)
   


app.run(debug=True)
