# Lab03 - Blog (app.py)
# Fran Kappes

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Dog Blog'
    return render_template('index.html', posts=posts)

posts = [
    {
        'title': "Today my big dog jumped over my little dog",
        'author': "Hooza Goodboy",
        'date': "May 30th, 2021",
        'body': "Puppy kitty ipsum dolor sit good dog foot stick canary. Teeth Mittens grooming vaccine walk swimming nest good boy furry tongue heel furry treats fish. Cage run fast kitten dinnertime ball run foot park fleas throw house train licks stick dinnertime window. Yawn litter fish yawn toy pet gate throw Buddy kitty wag tail ball groom crate ferret heel wet nose Rover toys pet supplies. Bird Food treats tongue lick teeth ferret litter box slobbery litter box crate bird small animals yawn small animals shake slobber gimme five toys polydactyl meow."
    }, 
        {
        'title': "Mid-afternoon wrestle (grudge rematch)",
        'author': "Hooza Goodboy",
        'date': "May 29th, 2021",
        'body': "Turtle cage lazy cat foot lazy cat groom canary window tooth brush bedding lazy cat pet supplies turtle water dog shake pet supplies kitty. Walk bird harness wet nose meow harness grooming water dog lol catz water bedding toys bird seed fetch lazy cat. Parakeet scratcher brush biscuit lick dog tooth walk food lazy cat biscuit. Cockatiel Snowball kitten Rover ferret puppy."
    },
        {
        'title': "Post-breakfast wrestlemania",
        'author': "Hooza Goodboy",
        'date': "May 28th, 2021",
        'body': "Pet Food pet supplies gimme five puppy cage food feathers food heel feathers running pet gate walk lazy dog Spike. Good Boy park lazy dog walk kibble Scooby snacks licks canary. Maine Coon Cat walk catch water dog slobber chew scratcher ID tag litter tuxedo dog house lazy cat park. Dinnertime fetch throw feathers fleas tongue lazy cat lick throw kitten parrot hamster wag tail aquarium chew heel good boy lick feathers cockatiel."
    },
        {
        'title': "My dogs love to wrestle",
        'author': "Hooza Goodboy",
        'date': "May 27th, 2021",
        'body': "Wet Nose food ferret vaccine finch vaccination Scooby snacks string wagging barky tail head good boy pet gate meow good boy. Commands shake bird biscuit left paw finch bark ferret bark gimme five turtle fur canary. Water puppy dog lick kisses pet supplies slobber cat bird seed. Food sit biscuit groom tongue cage."
    }
]

app.run(debug=True)