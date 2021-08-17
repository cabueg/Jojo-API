import requests

testjson = {
    "name": "Josuke Higashikata",
    "stand": "Crazy Diamond",
    "namesake": ["Shine on you Crazy Diamond"]
}

r = requests.post("http://127.0.0.1:5000/characters",json=testjson)

print(r.status_code, r.reason)