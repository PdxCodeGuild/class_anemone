from flask import Flask, render_template
app = Flask(__name__)

posts = [
        {
        'title': 'Pirates life for me',
        'author': 'Jane Doe',
        'date': 'May 29th, 2022',
        'body': "Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters."
    },

    {
        'title': 'Out back west on the old trail',
        'author': 'Finugus Cornwallace',
        'date': 'April 9th, 2022', 
        'body': "Stop licking my hand, you horse's ass. Buster's in what we like to call a light to no coma. In laymans terms, it might be considered a very heavy nap. Look at us, crying like a bunch of girls on the last day of camp. What do you expect, Mother? I'm half machine! I'm a monster!!"
    },

    {
        'title': 'Watch out lassie',
        'author': 'Caterine Omally',
        'date': 'Feburary 4th, 2022',
        'body': "Pommy ipsum a fiver Shakespeare pompous ee bah gum ponce a week on Sunday, fried toast taking the mick terribly whizz The Hounds of Baskerville Essex girls. Doing my head in could be a bit of a git bull dog posh nosh wedding tackle balderdash half-inch it skive eton mess, chips on't goggle box bobby The Doctor nowt 'tis."
    },

    {
        'title': 'Move Beartrice!!!',
        'author': 'Gerald Moofisus',
        'date': 'March 18th, 2022',
        'body': "Richmond tigers prahran hipsters, avalon is so not melb a macaron connoisseur world's most liveable city rooftop cinema melbourne central, graffiti street art dame edna cumulus inc ticket inspector, food bloggers the espy running the tan bourke st mall presets, essendon bombers east brunswick club ac/dc."
    }
]


@app.route('/')
def index():
    return render_template('index.html', posts=posts)

app.run(debug=True)