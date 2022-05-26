from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def invoke():
    return "Hello World"

app.run(debug=True)