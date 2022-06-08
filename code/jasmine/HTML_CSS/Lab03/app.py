from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "Coffee Anyone?",
        'author': "Coffee Ipsum",
        'date': "December 17, 2022",
        'body': "Decaffeinated, so aroma saucer, extraction so, in sit dark et organic. Espresso, et ut froth et doppio mazagran. Whipped café au lait trifecta skinny seasonal viennese steamed acerbic and cinnamon. Galão, plunger pot bar , sweet plunger pot brewed chicory est to go galão robusta. Black trifecta, turkish cappuccino single origin saucer, flavour variety cup frappuccino affogato sugar. Percolator whipped wings milk, black, iced, frappuccino foam breve irish affogato robust. That as, that, qui, con panna fair trade frappuccino ut to go coffee.Lungo so that coffee, acerbic, cup eu americano saucer robust. Coffee turkish frappuccino iced so ristretto java as dripper. Aged saucer, in as breve est ristretto. Brewed shop grinder so cortado, carajillo pumpkin spice whipped a filter."
    }, {
        'title': "Hello, IT",
        'author': "IT Crowd Ipsum",
        'date': "February 11, 2021",
        'body': "Uh... okay, well, the button on the side, is it glowing? Dear Sir stroke Madam, I am writing to inform you of a fire which has broken out at the premises of... Hello, IT. Have you tried turning it off and on again? So, remember the new number! 0118 999! 88199, 9119 725! ... 3! Oh my God. I didn't even know Smarties made a cereal. They don't. It's just Smarties in a bowl with milk. Today I have a business empire the like of which the world has never seen the like of which. I hope it doesn't sound arrogant when I say that I am the greatest man in the world! I mean, they have no respect for us up there! No respect whatsoever! We're all just drudgeons to them! No, no there you go, no there you go. I just heard it come on. Yeah, you do know how a button works don't you? No, not on clothes. 0115... no... 0118... no... 0118 999 ... 3. Hello? Is this the emergency services? Then which country am I speaking to? Hello? Hello? Yeah, you do know how a button works don't you? No, not on clothes. Yeah, you need to turn it on... uh, the button turns it on."
    }, {
        'title': "Take me to Space!",
        'author': "Space Ipsum",
        'date': "April 11, 2022",
        'body': "There is no strife, no prejudice, no national conflict in outer space as yet. Its hazards are hostile to us all. Its conquest deserves the best of all mankind, and its opportunity for peaceful cooperation many never come again. But why, some say, the moon? Why choose this as our goal? And they may well ask why climb the highest mountain? Why, 35 years ago, fly the Atlantic? Why does Rice play Texas? We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organize and measure the best of our energies and skills, because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win, and the others, too."
    }, {
        'title': "Give me the wine",
        'author': "Wine Ipsum",
        'date': "July 5, 2020",
        'body': "Be not offended when your ex drinks wine. How do you hold a wine glass? There is a right and a wrong way. Take a sip of wine and hold it in your mouth for a few seconds, then either swallow it or spit out.The pink color can range from a pale orange to a vivid near-purple, depending on the varietals used and wine-making techniques. Let mature reds breathe for twenty to thirty minutes, if you can. Serve dry Semillon with clams, mussels, or pasta salad. Alsace, in Eastern France, is highly regarded as a winemaking region. Egg whites are sometimes used in the clarification process. Cork it!"
    }
]


@app.route('/')
def index():
    return render_template('index.html', posts=posts)

app.run(debug=True)