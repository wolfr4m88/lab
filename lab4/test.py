import requests
import time

messages = ["msg1", "msg2", "msg3", "msg4", "msg5", "msg6", "msg7", "msg8", "msg9", "msg10"]
for msg in messages:
    response = requests.post("http://localhost:5000/message", json={"msg": msg})
    print(response.json())
    time.sleep(1)
for _ in range(10):
    response = requests.get("http://localhost:5000/message")
    print(response.json())
    time.sleep(1)
