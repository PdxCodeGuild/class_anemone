from creative.pyble import bible



text = bible.get_chapter()

print(text)


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(text):
    book= text
    # name = 'Jack'
    # temperature = 67
     
    return render_template('index.html', book=book)

app.run(debug=True)