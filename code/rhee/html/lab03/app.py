from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {   
        'title': 'RV Designs',
        'author': 'Daniel Perez',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sagittis orci a scelerisque purus semper eget. Nullam eget felis eget nunc lobortis mattis aliquam faucibus. Vehicula ipsum a arcu cursus vitae congue mauris. Pellentesque habitant morbi tristique senectus et. At quis risus sed vulputate odio. Amet nisl purus in mollis nunc. Sit amet nisl suscipit adipiscing. Amet tellus cras adipiscing enim. Sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra.',
        'date_posted': 'April 20, 2018'
    },
    {
        'title': 'On the Highways',
        'author': 'Chris Helios',
        'content': 'Sit amet nisl suscipit adipiscing. Amet tellus cras adipiscing enim. Sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra. Adipiscing elit pellentesque habitant morbi tristique senectus et netus et. Rhoncus est pellentesque elit ullamcorper dignissim. Turpis in eu mi bibendum neque egestas congue quisque egestas. Velit egestas dui id ornare arcu odio ut sem. Consequat ac felis donec et odio pellentesque diam volutpat commodo.',
        'date_posted': 'April 21, 2018'
    },
    {
        'title': 'East Coast',
        'author': 'Jane Doe',
        'content': 'Sit amet nisl suscipit adipiscing. Amet tellus cras adipiscing enim. Sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra. Adipiscing elit pellentesque habitant morbi tristique senectus et netus et. Rhoncus est pellentesque elit ullamcorper dignissim. Turpis in eu mi bibendum neque egestas congue quisque egestas. Velit egestas dui id ornare arcu odio ut sem. Consequat ac felis donec et odio pellentesque diam volutpat commodo.',
        'date_posted': 'April 21, 2018'
    },
    {
        'title': 'Going through Texas',
        'author': 'Mike Blank',
        'content': 'Sit amet nisl suscipit adipiscing. Amet tellus cras adipiscing enim. Sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra. Adipiscing elit pellentesque habitant morbi tristique senectus et netus et. Rhoncus est pellentesque elit ullamcorper dignissim. Turpis in eu mi bibendum neque egestas congue quisque egestas. Velit egestas dui id ornare arcu odio ut sem. Consequat ac felis donec et odio pellentesque diam volutpat commodo.',
        'date_posted': 'April 21, 2018'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/pictures")
def pictures():
    
    return render_template('pictures.html')


if __name__ == '__main__':
    app.run(debug=True)
