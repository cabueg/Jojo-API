from app import Character
from app import db
import json

db.create_all()

testjson = {
    "name": "Josuke Higashikata",
    "stand": "Crazy Diamond",
    "namesake": ["Shine on you Crazy Diamond"]
}

character = Character(name = testjson['name'],
                      stand = testjson['stand'],
                      namesake = testjson['namesake'])

db.session.add(character)
db.session.commit()