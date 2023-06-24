import requests

base_url = "http://localhost:5000/message"
messages = ["msg1", "msg2", "msg3", "msg4", "msg5", "msg6", "msg7", "msg8", "msg9", "msg10"]
print("Posting messages:")
for msg in messages:
    response = requests.post(base_url, json={"msg": msg})
    print("Status code:", response.status_code)
    print("Response:", response.json())
print("Getting messages:")
response = requests.get(base_url)
print("Status code:", response.status_code)
print("Response:", response.json())
print("Getting messages after shutdown:")
response = requests.get(base_url)
print("Status code:", response.status_code)
print("Response:", response.json())
