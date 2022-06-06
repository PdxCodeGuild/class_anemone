from flask import Flask, render_template, redirect, request
from jsondb import JsonDB
import pprint

app = Flask(__name__)

# blank = JsonDB('blank.json')
# blank.load()
# blank.save()

db = JsonDB('db.json')
db.load()

@app.route('/', methods=['GET', 'POST'])

def index():
    
    burrito_order_form = db.get('burrito order form')
    customer_info = burrito_order_form['customer info']
    order_info= burrito_order_form['order info']
    tortilla = order_info['tortilla']
    # print(order_info, tortilla)
    rice = order_info['rice']
    beans = order_info['beans']
    protein = order_info['protein']
    additional_ingred = order_info['additional ingredients']
    # print(rice)
    if request.method == 'POST':
        print(request.form)


        tortilla_order = request.form['tortilla']
        rice_order = request.form['rice']
        beans_order = request.form['beans']
        protein_order = request.form['protein']
        for key in request.form:
            if key == 'cheese':
                additional_ingred['cheese'] += int(request.form[key])
            elif key == 'sour-cream':
                additional_ingred['sour-cream'] += int(request.form[key])

        # cheese = request.form['cheese']
        # sour_cream = request.form['sour-cream']
        # additional_ingred_order=
        # print(tortilla)
        name = request.form['name']
        password = request.form['password']
        delivery = request.form['delivery']
        dict_list = {}

        customer_info['name']=name
        customer_info['password']=password
        customer_info['delivery']=delivery
        tortilla[tortilla_order]+=1
        rice[rice_order]+=1
        beans[beans_order]+=1
        protein[protein_order]+=1
        # additional_ingred[additional_ingred_order]+=1
        
        dict_list.update({'customer info':customer_info})
        dict_list.update({'order info': {'tortilla':tortilla, 'rice':rice,'beans':beans,'protein': protein, 'additional ingredients': additional_ingred}})
        db.set("burrito order form", dict_list)
        db.save()
        return render_template("form.html", customer_info=customer_info, order_info=order_info)
    elif request.method == 'GET':
        blank = JsonDB('blank.json')
        blank.load()
        burrito_order_form = blank.get('burrito order form')
        customer_info = burrito_order_form['customer info']
        order_info= burrito_order_form['order info']
        db.load()
        dict_list={}
        dict_list.update({'customer info':customer_info})
        dict_list.update({'order info':order_info})
        db.set("burrito order form", dict_list)
        db.save()
        return render_template("form.html", customer_info=customer_info, order_info=order_info)
    

app.run(debug=True)