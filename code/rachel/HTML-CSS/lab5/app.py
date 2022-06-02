from flask import Flask, render_template, request
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phrase = list(request.form['phrase'])
        abc = list(string.ascii_letters)

        new_word = ''

        for letter in phrase:
            letter_index = abc.index(letter)
            new_index = letter_index + 13
            if new_index > 25:
                new_index -= 26
                # print(new_index)
            cipher = abc[new_index]
            new_word += cipher
            # print (cipher)
        # print (new_word)
        return render_template("index.html", word=new_word)
    return render_template("index.html")

app.run(debug=True)
