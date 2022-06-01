from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "My Favorite Toys",
        'author': "Cali",
        'date': "April 14, 2021",
        'body': "Cheese on toast queso pepper jack. Manchego danish fontina paneer cheesy grin boursin mascarpone mozzarella cheese slices. Pepper jack roquefort st. agur blue cheese who moved my cheese squirty cheese fromage st. agur blue cheese mozzarella. Cauliflower cheese cheese triangles goat.",
    },
    {
        'title': "Treats That Make My Tail Wag Extra Fast!",
        'author': "Cali",
        'date': "June 6, 2021",
        'body': "Fromage frais cheese and biscuits stinking bishop. Parmesan brie when the cheese comes out everybody's happy cheese and biscuits dolcelatte squirty cheese airedale camembert de normandie. Cheesecake croque monsieur manchego port-salut emmental melted cheese boursin melted cheese. Mascarpone cream cheese cottage cheese lancashire stinking bishop lancashire the big cheese jarlsberg. Cottage cheese cheesy feet paneer who moved my cheese danish fontina st. agur blue cheese camembert de normandie monterey jack. Mozzarella croque monsieur macaroni cheese paneer cheddar say cheese smelly cheese stilton. Rubber cheese cheesy feet halloumi stinking bishop cheeseburger halloumi taleggio macaroni cheese. Halloumi lancashire emmental brie babybel fromage cauliflower cheese fromage. Cheese and biscuits cheesy grin queso jarlsberg blue castello smelly cheese stilton cheesecake. Cheese triangles who moved my cheese.",
    },
    {
        'title': "Why My Human Is The Best Human",
        'author': "Cali",
        'date': "October 27, 2021",
        'body': "Airedale chalk and cheese cheesy grin. Cream cheese who moved my cheese cheese triangles airedale cut the cheese queso cheesy grin caerphilly. Brie camembert de normandie cheesy grin chalk and cheese the big cheese danish fontina everyone loves feta. Everyone loves boursin croque monsieur jarlsberg caerphilly cheese and wine red leicester roquefort. Ricotta ricotta. Brie caerphilly fondue. Cream cheese queso croque monsieur say cheese cheesy grin dolcelatte cheeseburger mozzarella. Fondue ricotta dolcelatte cheeseburger everyone loves cheesy feet paneer queso. Edam cream cheese bavarian bergkase the big cheese port-salut cheese slices camembert de normandie queso. Ricotta.",
    },
    {
        'title': "My Pawsome Birthday Party!",
        'author': "Cali",
        'date': "April 29, 2022",
        'body': "Blue castello pecorino stinking bishop. Port-salut stilton stilton feta mascarpone stinking bishop when the cheese comes out everybody's happy cut the cheese. Cheesy grin jarlsberg cauliflower cheese mozzarella goat macaroni cheese goat the big cheese. Pepper jack cow boursin croque monsieur cheese triangles cheesy feet airedale caerphilly. Emmental cheesecake stinking bishop hard cheese taleggio lancashire cut the cheese jarlsberg. Boursin bocconcini croque monsieur.Red leicester paneer chalk and cheese. Halloumi who moved my cheese bavarian bergkase the big cheese croque monsieur mascarpone cauliflower cheese fromage. Paneer everyone loves cheeseburger lancashire parmesan mascarpone port-salut camembert de normandie. The big cheese rubber cheese dolcelatte brie cheese and wine goat cheese and biscuits swiss. Hard cheese airedale halloumi manchego danish fontina parmesan cheese and wine cauliflower cheese. Pecorino lancashire edam blue castello cheese slices cheeseburger red leicester the big cheese. Ricotta lancashire cheddar queso paneer st. agur blue cheese macaroni cheese babybel. Feta.",
    }
]

@app.route('/')
def index():

    return render_template('index.html', posts=posts)

app.run(debug=True)