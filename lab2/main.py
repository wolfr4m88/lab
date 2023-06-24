import requests
import json

url = 'http://localhost:5000/message'
get_url = 'http://localhost:5000/messages'

# POST-запити до facade-service
messages = ["Hello", "World"]
payload = {'messages': messages}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)
data = response.json()
print("POST Response:")
print(data)

# GET-запит до facade-service
response = requests.get(get_url)
data = response.json()
print("GET Response from facade-service:")
print(data)

# GET-запит до logging-service
logging_url = 'http://localhost:5001/logs'
response = requests.get(logging_url)
data = response.json()
print("GET Response from logging-service:")
print(data)
