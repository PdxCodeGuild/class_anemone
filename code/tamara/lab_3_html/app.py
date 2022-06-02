from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    posts = [
        {
            'title': "Title 1!",
            'author': 'Selvester Stalone',
            'date': '05/22/2022',
            'body': 'Sweet chocolate tiramisu I love I love. I love sesame snaps chocolate cake I love wafer candy canes. Lollipop I love carrot cake I love danish sweet roll. Gingerbread I love oat cake chocolate cake pudding I love. Dessert sesame snaps pie pudding sweet roll brownie jelly beans gummi bears brownie. Carrot cake jelly-o I love liquorice liquorice carrot cake.'
        },
        {
            'title': "Title 2!",
            'author': 'Jane Goodall',
            'date': '05/22/2055',
            'body': 'I love marshmallow lollipop danish topping macaroon. Marzipan candy canes I love dragée tart toffee. Icing gingerbread candy canes marzipan danish I love brownie cotton candy. Bear claw danish soufflé pastry sesame snaps. Tiramisu jelly chocolate cake icing sugar plum. Jujubes chocolate soufflé apple pie sesame snaps. I love bonbon lemon drops lemon drops chocolate icing candy. Sugar plum caramels danish gingerbread tart sweet roll jujubes I love. Oat cake sweet jelly-o I love wafer pudding lollipop jelly. I love halvah halvah liquorice soufflé.'
        },
        {
            'title': "Title 3!",
            'author': 'Rick James',
            'date': '05/22/2111',
            'body': 'Sesame snaps icing I love croissant sugar plum wafer liquorice. Sugar plum marshmallow sesame snaps pie sweet jelly-o ice cream. Chocolate bar cupcake sesame snaps macaroon ice cream pudding candy. Toffee sweet roll chupa chups chocolate bar pudding bear claw tootsie roll muffin. Fruitcake jelly beans cake tart lollipop chupa chups powder marzipan I love. Chocolate cake I love caramels muffin pie jelly-o dragée cupcake. Candy canes sugar plum halvah jelly-o sweet roll jelly-o candy. Cake cheesecake tiramisu lemon drops gummi bears apple pie marzipan fruitcake chocolate.'
        },
        {
            'title': "Title 4!",
            'author': 'Ms. Author',
            'date': '02/22/2222',
            'body': 'Powder sesame snaps candy canes halvah chocolate jelly beans. I love sugar plum jujubes croissant cotton candy macaroon. Bear claw marshmallow pudding chocolate bar pie dragée brownie. Powder I love sesame snaps I love apple pie brownie biscuit macaroon. Cookie donut danish I love cheesecake carrot cake. Liquorice bear claw sweet roll brownie sweet tiramisu. Liquorice cupcake sweet I love jujubes.'
        }
    ]
    
    return render_template('index.html', posts=posts)

app.run(debug=True)