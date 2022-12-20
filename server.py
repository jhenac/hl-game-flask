from flask import Flask
import random

random_number = random.randint(0,9)

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy-downsized-large.gif'>"

@app.route('/<int:number>')
def guess_number(number):
    if number > random_number:
        return "<h1 style='color: red'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/LoQSLWUbdmjp64zXYA/giphy.gif'>"
    elif number < random_number:
        return "<h1 style='color: purple'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/Y4z9olnoVl5QI/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/td02jbtsXIxpBv45rJ/giphy.gif'>"

if __name__ == '__main__':
    app.run(debug=True)