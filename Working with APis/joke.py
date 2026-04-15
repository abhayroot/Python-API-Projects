import requests
import json

response = requests.get("https://v2.jokeapi.dev/joke/Any?format=json&type=single")
jokes = json.loads(response.content)
jokes1 = jokes["joke"]
print(jokes1)