from distutils.debug import DEBUG
from flask import Flask,render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def number_input():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        from_units = request.form['from-units']
        to_units = request.form['to-units']
        distance = float(request.form['distance'])

        if from_units == 'ft':
            result = distance * 0.3048
        elif from_units == 'mi':
            result = distance * 1609.34
        elif from_units == 'm':
            result = distance
        elif from_units == 'km':
            result = distance * 1000
        elif from_units == 'yard':
            result = distance * 0.9144
        elif from_units == 'inch':
            result = distance * 0.0254
        
 


        if to_units == 'ft':
            final_result=(result/0.3048)
        elif to_units == 'mi':
            final_result=(result/1609.34)
        elif to_units == 'm':
            final_result=(result)
        elif to_units == 'km':
            final_result=(result/1000)
        elif to_units == 'yard':
            final_result=(result/0.9144)
        elif to_units == 'inch':
            final_result=(result/0.0254)
        
        return render_template('index.html', final_result=final_result, to_units=to_units)




app.run(debug=True)