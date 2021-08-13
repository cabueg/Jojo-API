from enum import unique
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR']= True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///character.db'
db = SQLAlchemy(app)

class Character(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False)
    stand = db.Column(db.String(80), unique=True, nullable=False)
    namesake = db.Column(db.String(120))


# Work on this bit next time. The plan is to
# take the data that we got from the webscraping
# and implement it into the database and then 
# I could look at it on the server
