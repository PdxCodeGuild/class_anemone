from flask import Flask, render_template, request, redirect
from posts import posts
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', posts=posts)

app.run(use_reloader=True, debug=True)