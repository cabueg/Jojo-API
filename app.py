from enum import unique
from flask import Flask,request,jsonify
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR']= True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///character.db'
db = SQLAlchemy(app)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    stand = db.Column(db.String(255), nullable=True)
    namesake = db.Column(db.PickleType, nullable=True)

    def __repr__(self):
        return f"{self.name} - {self.stand} - {self.namesake}"


@app.route('/')
def index():
    return 'Jojo!'

#the website link + '/characters' will run the function below
@app.route('/characters')
def get_characters():
    #grabs all objects created from the class Character
    characters = Character.query.all()

    #create empty list
    output = []

    #for each character, create a dictionary with each object's data and append to list
    for character in characters:
        character_data = {'name': character.name, 
                          'stand': character.stand, 
                          'namesake': character.namesake}
        output.append(character_data)

    #return a dictionary with the list
    return {'characters': output} 

@app.route('/characters', methods=['POST'])
def add_character():
    character = Character(name = request.json['name'],
                          stand = request.json['stand'],
                          namesake = request.json['namesake'])
    db.session.add(character)
    db.session.commit()
    return {'id': character.id}


@app.route('/characters/<id>')
def get_character(id):
    character = Character.query.get_or_404(id)
    return {"name": character.name, 
            "stand": character.stand, 
            "namesake": character.namesake
            }


@app.route('/characters/<id>', methods=['DELETE'])
def delete_character(id):
    character = Character.query.get(id)
    if character is None:
        return {"error": "not found"}
    message = {"message": character.name + " just got ZA HANDED"}
    db.session.delete(character)
    db.session.commit()
    return message
