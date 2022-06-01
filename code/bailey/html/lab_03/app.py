from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': "Chillwave offal you probably haven't heard of them",
        'author': "Blogger McBlogface",
        'date': "October 14th, 2021",
        'body': "Godard mlkshk ethical XOXO knausgaard taiyaki narwhal sustainable portland tumblr mixtape sartorial. Slow-carb hashtag lumbersexual beard prism. Ennui deep v kombucha aesthetic, hammock jean shorts hashtag asymmetrical salvia. Pour-over DIY knausgaard 90's. Brunch squid cred adaptogen farm-to-table disrupt ugh flexitarian single-origin coffee marfa trust fund. Disrupt asymmetrical pabst, neutra skateboard hell of pop-up umami. Dreamcatcher skateboard put a bird on it, cred palo santo squid taiyaki air plant cliche green juice brooklyn post-ironic meditation butcher."
    },
    {
        'title': "Developer bingbong",
        'author': "Blogman",
        'date': "September 9th, 2009",
        'body': "The trouble with programmers is that you can never tell what a programmer is doing until it’s too late. (Seymour Cray) Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are–by definition–not smart enough to debug it. (Brian Kernighan) For a long time it puzzled me how something so expensive, so leading edge, could be so useless. And then it occurred to me that a computer is a stupid machine with the ability to do incredibly smart things, while computer programmers are smart people with the ability to do incredibly stupid things. They are, in short, a perfect match. (Bill Bryson) The cheapest, fastest, and most reliable components are those that aren’t there. (Gordon Bell)"
    },
    {
        'title': "Googflorps",
        'author': "Googflorpian mcgorgan",
        'date': "June 29th, 2021",
        'body': "A business big enough that it could be listed on the NASDAQ goes belly up. Disappears! It ceases to exist without me. No, you clearly don't know who you're talking to, so let me clue you in. I am not in danger, Skyler. I AM the danger! A guy opens his door and gets shot and you think that of me? No. I am the one who knocks! "
    },{
        'title': "Snakes on a plane",
        'author': "Samuel L Jackson",
        'date': "July 4th 2021",
        'body': "The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of darkness, for he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who would attempt to poison and destroy My brothers. And you will know My name is the Lord when I lay My vengeance upon thee."
    }
]


@app.route('/')
def index():
    
    return render_template('index.html', posts=posts)

app.run(debug=True)

