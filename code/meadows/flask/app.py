from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # main server .. can do @app.route('/about') and change def to about to get another page added
def index():
    return "<h1>Hello, World!</h1>" # main function

if __name__ == '__main__': # calling the app Varible below the import function
    app.run(debug=True) # running our app.py and applying our debug mode to it

#--------------------------------------------------------- VERSION 1 --------------------------------------------------------#