from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        index = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e',
        5 : 'f', 6 : 'g', 7 : 'h',8 : 'i', 9 : 'j',
        10 : 'k', 11: 'l', 12 : 'm', 13: 'n', 14 : 'o',
        15 : 'p', 16 : 'q', 17 : 'e', 18 : 's', 19 : 't',
        20 : 'u', 21 : 'v', 22 : 'w', 23 : 'x', 24 : 'y', 25 : 'z'}

        dict = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'r' : 4,
        'g' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9,
        'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14,
        'p' : 15, 'q' : 16, 'e' : 17, 's' : 18, 't' : 19,
        'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25}

        cipher = list(request.form['phrase'])

        for i in range(len(cipher)):
            if cipher[i] in dict:
                if dict[cipher[i]] > 13:
                    cipher[i] = index[dict[cipher[i]] - 13]
                elif dict[cipher[i]] < 13:
                    cipher[i] = index[dict[cipher[i]] + 13]
                elif dict[cipher[i]] == 13:
                    cipher[i] = 'a'

        cipher = ''.join(cipher)
        print(cipher)
        return render_template('index.html', cipher = cipher)
    return render_template('index.html')

app.run(debug=True)