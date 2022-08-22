# from tempfile import template
from flask import Flask, redirect, render_template
from requests import request

app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello World'

@app.route('/')
def blog():
    posts = [
    {
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Hemsworth",
        'date': "June 24th, 2020",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
    },
    {
        'title': "I dont know im still working on it",
        'author': "Kakashi",
        'date': "September 30th, 2021",
        'body': "The Internet? Is that thing still around? (Homer Simpson) The best thing about a boolean is even if you are wrong, you are only off by a bit. (Anonymous) A computer lets you make more mistakes faster than any invention in human history–with the possible exceptions of handguns and tequila. (Mitch Radcliffe) Computers are like bikinis. They save people a lot of guesswork. (Sam Ewing)"
    },
    {
        'title': "Life is crazy",
        'author': "Ichigo",
        'date': "August 10th, 2015",
        'body': "The key to more success is to get a massage once a week, very important, major key, cloth talk. They never said winning was easy. Some people can’t handle success, I can. How’s business? Boomin. Give thanks to the most high. We dont see them, we will never see them. You see the hedges, how I got it shaped up? Its important to shape up your hedges, its like getting a haircut, stay fresh. Find peace, life is like a water fall, youve gotta flow. Lets see what Chef Dee got that they dont want us to eat"
    },
    {
        'title': "Coffee in Britian",
        'author': "Luffy",
        'date': "October 14th, 2007",
        'body': "Body, wings, sit, aftertaste galão as chicory flavour robusta. Strong white, ut sugar, cortado con panna brewed foam café au lait foam. Single shot mocha aged crema saucer et frappuccino. Blue mountain caffeine single origin roast froth arabica in cinnamon kopi-luwak french press."
    },
    {
        'title': "Why Ill never buy another mop",
        'author': "Saiki",
        'date': "October 25th, 2018",
        'body': "Godfather ipsum dolor sit amet. We're both part of the same hypocrisy, senator, but never think it applies to my family. I don't feel I have to wipe everybody out, Tom. Just my enemies. This one time, this one time I'll let you ask me about my affairs. Never let anyone know what you are thinking. You can act like a man!"


    },
    {
        'title': "How to become less crazy",
        'author': "Momo",
        'date': "May 5th, 2014",
        'body': "Biscuit pastry lollipop carrot cake dragée tiramisu chocolate cake muffin chupa chups. Bonbon sweet roll bonbon dragée powder tootsie roll. Danish lemon drops tart chocolate bar pastry topping dessert cupcake soufflé."
    }
    ]
    return render_template('blog.html',author = 'Faith',  posts=posts)



if __name__ == '__main__':
    app.run()

