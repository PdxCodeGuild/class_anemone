from flask import Flask,render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', )

@app.route('/', methods=['GET','POST'])
def number_input():
    distance = request.form['distance']
    processed_text = distance.upper()
    return processed_text
          


app.run()