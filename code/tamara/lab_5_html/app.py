from flask import Flask, render_template, redirect, request
from rot import ROT13

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method=="POST":
        user_string = request.form['user_string']
        encryption = ROT13(user_string)
        return render_template("index.html", user_string = user_string, encryption=encryption)

    return render_template("index.html")

app.run(debug=True)
