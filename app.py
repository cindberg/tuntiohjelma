from flask import Flask, jsonify, request, session, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

POSTGRES_URL = 'localhost'
POSTGRES_USER = 'postgres'
POSTGRES_PW = 'admin'
POSTGRES_DB = 'postgres'
DB_URL = 'postgresql+psycopg2://{user}:{password}@{url}/{db}'.format(user=POSTGRES_USER,
                                                                     password=POSTGRES_PW,
                                                                     url=POSTGRES_URL,
                                                                     db=POSTGRES_DB)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SECRET_KEY'] = 'admin1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # hiljentää muistutukset, (turha voi poistaa)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=60)  # (turha lisä voi poistaa)
CORS(app)

db = SQLAlchemy(app)

if __name__ == "__main__":
    from views import *

    app.run(debug=True, port=5002)
