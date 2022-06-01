from flask import Flask, render_template
app = Flask(__name__)
import random
import string

# def random_characters(length, alphabet):
#     output = ''
#     for i in range(length):
#         char = random.choice(alphabet)
#         output += char
#     return output

# def random_password(n_lowercase, n_uppercase, n_digits, n_punct):
#     output = ''
#     output += random_characters(n_lowercase, string.ascii_lowercase)
#     output += random_characters(n_uppercase, string.ascii_uppercase)
#     output += random_characters(n_digits, string.digits)
#     output += random_characters(n_punct, string.punctuation)
#     output = list(output)
#     random.shuffle(output)
#     output = ''.join(output)
#     return output

# print(random_password(20))

def random_password(length):
    characters = string
    n = int(input('Enter password length: '))
    password = ''
    for i in range(n):
        password += random.choice(characters)
    return password



@app.route('/')
def index():
    
    return render_template('index.html')



app.run(debug=True)
