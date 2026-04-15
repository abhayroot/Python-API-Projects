import requests
import json
import logging

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

url = "https://v2.jokeapi.dev/joke/Any?format=json&type=single"

try:
    logging.info("Request started")

    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        data = response.json()

        if "joke" in data:
            joke = data["joke"]
            logging.info("Request successful")
            logging.info(f"Joke: {joke}")
            print(joke)
        else:
            logging.error("Key 'joke' not found in response")
            print("Unexpected response format")

    else:
        logging.error(f"Failed with status code: {response.status_code}")
        print("Failed to get joke")

except requests.exceptions.RequestException as e:
    logging.error(f"Request failed: {e}")
    print("Error occurred during API call")

finally:
    logging.info("Execution finished")
    print("exited")