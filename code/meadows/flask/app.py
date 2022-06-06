from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # main server .. can do @app.route('/about') and change def to about to get another page added
# def index():
#     return render_template('index_html')

def blog():

    post = [{
            'title': "What is Lorem Ipsum?",
            'author': "Lorem Ipsum",
            'date': "3/6/2012",
            'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        }, 
        {
            'title': "What is Godfather?",
            'author': "Godfather Ipsum",
            'date': "8/16/2019",
            'body': "Godfather ipsum dolor sit amet. When they come... they come at what you love. I don't feel I have to wipe everybody out, Tom. Just my enemies. Never let anyone know what you are thinking. Only don't tell me you're innocent. Because it insults my intelligence and makes me very angry. What's wrong with being a lawyer?I don't like violence, Tom. I'm a businessman; blood is a big expense. Fredo, you're my older brother, and I love you. But don't ever take sides with anyone against the Family again. Ever. I know it was you, Fredo. You broke my heart. You broke my heart! Don't ever give an order like that again. Not while I'm alive. Vito, how do you like my little angel? Isn't she beautiful?"
        }, 
        {
            'title': "Major Keys to Success",
            'author': "Khaled Ipsum",
            'date': "6/23/2021",
            'body': "Lorem Khaled Ipsum is a major key to success. It’s important to use cocoa butter. It’s the key to more success, why not live smooth? Why live rough? To succeed you must believe. When you believe, you will succeed. Always remember in the jungle there’s a lot of they in there, after you overcome they, you will make it to paradise. Hammock talk come soon. The key to success is to keep your head above the water, never give up. Wraith talk. They will try to close the door on you, just open it.Let me be clear, you have to make it through the jungle to make it to paradise, that’s the key, Lion! How’s business? Boomin. Surround yourself with angels, positive energy, beautiful people, beautiful souls, clean heart, angel. Congratulations, you played yourself. Cloth talk. In life you have to take the trash out, if you have trash in your life, take it out, throw it away, get rid of it, major key. The key to more success is to have a lot of pillows."
        }, 
        {
            'title': "Give your project a caffeine kick!",
            'author': "Coffee Ipsum",
            'date': "1/28/2012",
            'body': "Cup steamed single origin coffee single origin irish to go half and half redeye rich. Half and half plunger pot, americano single origin robusta french press sweet coffee. Espresso frappuccino, aromatic, cortado aroma irish breve that. Con panna, decaffeinated, turkish rich blue mountain half and half, mug turkish arabica strong cup pumpkin spice.Whipped medium, skinny, robust mocha doppio galão saucer turkish robusta. Flavour, iced grounds, caramelization saucer turkish strong frappuccino. A sit decaffeinated, chicory half and half viennese at flavour cream. Foam affogato rich macchiato trifecta, aftertaste aroma single origin so strong variety."
        },{
            'title': "Put A Cheeseburger In Your Ipsum",
            'author': "Viral Foundry",
            'date': "11/13/2022",
            'body': "Cheeseburgers make your knees weak and your soul tingle.A great cheeseburger is a gastronomical event with so many varieties you couldn’t get tired of it if you tried.There’s cheesy incarnation waiting for you no matter what your palate preferences are.Unless you’re vegan, in which case we’re sorry for your loss."
        }]
    return render_template('index.html', post = post)
# if __name__ == '__main__': # calling the app Varible below the import function
app.run(debug=True) # running our app.py and applying our debug mode to it

#--------------------------------------------------------- VERSION 2 --------------------------------------------------------#