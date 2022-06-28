from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
      posts = [{
        'title': 'FF6 is Here! ',
        'image': 'https://novacrystallis.com/wp-content/uploads/2022/03/FF6-Pixel-Remaster-Header.jpg',
        'content': 'Final Fantasy VI,[a] also known as Final Fantasy III from its initial North American release, is a 1994 role-playing video game developed and published by Square for the Super Nintendo Entertainment System. It is the sixth main entry in the Final Fantasy series, and the first to be directed by someone other than series creator Hironobu Sakaguchi; the role was instead filled by Yoshinori Kitase and Hiroyuki Ito. Long-time collaborator Yoshitaka Amano returned as character designer and concept artist, while composer Nobuo Uematsu returned to compose the games score, which has been released on several soundtrack albums..'
    },
    {
        'title': 'Elden Ring is Here!',
        'image': 'https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Elden_Ring_Box_art.jpg/220px-Elden_Ring_Box_art.jpg',
        'content': 'Elden Ring[a] is an action role-playing game developed by FromSoftware and published by Bandai Namco Entertainment. The game was directed by Hidetaka Miyazaki and made in collaboration with fantasy novelist George R. R. Martin, who provided material for the games setting. It was released for Microsoft Windows, PlayStation 4, PlayStation 5, Xbox One, and Xbox Series X/S on February 25, 2022. '
    },
    {
        'title': 'Tekken 7 is Here!',
        'image': 'https://upload.wikimedia.org/wikipedia/en/thumb/1/17/Official_Tekken_7_Logo.jpg/220px-Official_Tekken_7_Logo.jpg',
        'content': 'Tekken 7 (鉄拳7) is a fighting game developed and published by Bandai Namco Entertainment. It is the seventh main and ninth overall installment in the Tekken series. Tekken 7 had a limited arcade release in March 2015. An updated arcade version, Tekken 7: Fated Retribution, was released in July 2016, and features expanded content including new stages, costumes, items and characters.[3] The home versions released for PlayStation 4, Xbox One and Microsoft Windows in June 2017 were based on Fated Retribution.[4] '
    },
    {
        'title': 'Super Bomberman is Here!',
        'image': 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Super.Bomberman.Box.Art.SNES.PAL.png/220px-Super.Bomberman.Box.Art.SNES.PAL.png',
        'content': 'Super Bomberman[b] is an action, maze game, part of the Bomberman series, released for the Super NES in 1993. It is the first in the series to be released in Europe keeping the Bomberman title instead of being called Dynablaster or Eric and the Floaters. '
    },
        ]


      return render_template('index.html', posts = posts )

app.run(debug=True)


'''

app = Flask(__name__)



@app.route('/')
def index():
    name = 'myname'
    return render_template('index.html', name=name)


app.run(debug=True)
'''