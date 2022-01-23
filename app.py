from flask import Flask

app = Flask(__name__)


@app.route('/')

def koti():  # etusivu

    return 'Työnseuranta'

def ominaisuudet(): #featuret

    return 'Ominaisuudet!'





if __name__ == '__main__':
    app.run()
