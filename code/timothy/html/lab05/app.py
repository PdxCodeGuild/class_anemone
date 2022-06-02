import randoms
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
object = randoms.Randoms()

@app.route('/', methods=('GET', 'POST'))
def index():
    # if request.method == 'POST':

    return render_template('index.html')

app.run(debug=True)


# RNDM GEN
# uppers = int(input('How many Uppercase Chars in new password: '))
# lowers = int(input('How many Lowercase Chars in new password: '))
# nums = int(input('How many Number Chars in new password: '))
# special = int(input('How many Special Chars in new password: '))

# random_password(lowers, uppers, nums, special)

