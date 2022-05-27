from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def invoke():
    posts = [
        {
            'title': 'For the party',
            'author': 'PoH',
            'date': 'August 24, 2032',
            'body': "Godfather ipsum dolor sit amet. Don't ever give an order like that again. Not while I'm alive. Very well. You want to do business with me. I will do business with you. Vito, how do you like my little angel? Isn't she beautiful? Friends and money - oil and water. It's a Sicilian message. It means Luca Brasi sleeps with the fishes."
        }, {
            'title': 'After the party',
            'author': 'XaXa',
            'date': 'August 25, 2032',
            'body': "Why did you go to the police? Why didn't you come to me first? What's the matter with you? Is this what you've become, a Hollywood finocchio who cries like a woman? 'Oh, what do I do? What do I do?' What is that nonsense? Ridiculous! What's the matter with you, huh? What am I going to do? Am I going to make that baby an orphan before he's born? My father's name was Antonio Andolini... and this is for you"
        }, {
            'title': 'Problems',
            'author': 'Lux',
            'date': 'August 27, 2032',
            'body': "Your enemies always get strong on what you leave behind. Te salut, Don Corleone. Do me this favor. I won't forget it. Ask your friends in the neighborhood about me. They'll tell you I know how to return a favor. My father taught me many things here - he taught me in this room. He taught me: keep your friends close, but your enemies closer."
        }, {
            'title': 'Crap Baskets',
            'author': 'Johnny Black (Meattabogin)',
            'date': 'August 27, 2032',
            'body':  "Te salut, Don Corleone. What's the matter with you, huh? What am I going to do? Am I going to make that baby an orphan before he's born? Why did you go to the police? Why didn't you come to me first? Leave the gun. Take the cannoli. If anything in this life is certain, if history has taught us anything, it is that you can kill anyone."
        }
    ]
    # for i, post in enumerate(posts):
    #     title = ''
    #     author = ''
    #     date =''
    #     body = ""
    #     for post in posts[i]:
    #         title.


    return render_template('index.html', posts=posts)
    

app.run(debug=True)