import json
import re
import requests, json

res = requests.get('https://api.chucknorris.io/jokes/random')

joke = json.loads(res.text)

print(joke['value'])