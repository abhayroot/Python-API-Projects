import requests
import os
import json
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# First API call with reasoning
token = os.getenv("API_token")
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": (f"Bearer {token}"),
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "arcee-ai/trinity-large-preview:free",
    "messages": [
        {
          "role": "user",
          "content": "how is strawberry spelled'?"
        }
      ],
    "reasoning": {"enabled": True}
  })
)

response = response.json()
response = response['choices'][0]['message']

# Preserve the assistant message with reasoning_details
messages = [
  {"role": "user", "content": "how is strawberry spelled? how many r is there"},
  {
    "role": "assistant",
    "content": response.get('content'),
    "reasoning_details": response.get('reasoning_details')  # Pass back unmodified
  },
  {"role": "user", "content": "Are you sure? Think carefully."}
]

# Second API call - model continues reasoning from where it left off
response2 = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": (f"Bearer {token}"),
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "arcee-ai/trinity-large-preview:free",
    "messages": messages,  # Includes preserved reasoning_details
    "reasoning": {"enabled": True}
  })
)

response2 = response2.json()
response2 = response2['choices'][0]['message']

print(response.get('content'))
print(response2.get('content'))
