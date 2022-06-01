from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # main server .. can do @app.route('/about') and change def to about to get another page added
# def index():
#     return render_template('index_html')
def home():
    return render_template('order.html')


if __name__ == '__main__':
    app.run(debug=True)