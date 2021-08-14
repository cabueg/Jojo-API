import requests

testjson = {
    "name": "Koichi Hirose",
    "stand": "Echoes",
    "namesake": ["Echoes", "The Hirose River"]
}
r = requests.post("http://127.0.0.1:5000/characters",json=testjson)

print(r.status_code, r.reason)