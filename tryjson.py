from enum import unique
from flask import Flask,request,jsonify
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR']= True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poop.db'
db = SQLAlchemy(app)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json_column = db.Column(JSON)


def insert_data():
    example2 = Character(json_column={
                "name": "Koichi Hirose",
                "stand": "Echoes",
                "namesake": ["The Hirose River", "Echoes"]
    })
    db.session.add(example2)
    db.session.commit()

def query(id):
    example = Character.query.get_or_404(id)
    print(example)
    print(example.json_column)
    print(type(example.json_column))


query(2)