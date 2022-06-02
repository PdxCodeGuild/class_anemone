
import randoms
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
object = randoms.Randoms()

pword = []
# x = ''.join(pword)
# pstring = x
# print(pstring)

@app.route('/', methods=('GET', 'POST'))
def index():
    
    if request.method == 'POST':
        uppers = int(request.form['uppercase'])
        lowers = int(request.form['lowercase'])
        nums = int(request.form['numbers'])
        special = int(request.form['special'])
        password = object.random_password(uppers, lowers, nums, special)
        pword.append(password)
        return redirect('/user.html')

    return render_template('index.html')

@app.route('/user.html', methods=['GET'])
def user():

    ps = pword[0]
    print('password', pword)
    return render_template('user.html', ps=ps)


app.run(debug=True)


# RNDM GEN
# uppers = int(input('How many Uppercase Chars in new password: '))
# lowers = int(input('How many Lowercase Chars in new password: '))
# nums = int(input('How many Number Chars in new password: '))
# special = int(input('How many Special Chars in new password: '))

# random_password(lowers, uppers, nums, special)

