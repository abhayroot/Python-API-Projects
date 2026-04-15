import requests
import json
import logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
response = requests.get("https://v2.jokeapi.dev/joke/Any?format=json&type=single")
jokes = json.loads(response.content)
jokes1 = jokes["joke"]
logging.info(jokes1)
print(jokes1)