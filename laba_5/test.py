import requests
import random
import string

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

for _ in range(10):
    msg = random_string(5)
    response = requests.post("http://localhost:5000/message", json={"msg": msg})
    print(response.json())

response = requests.get("http://localhost:5000/message")
print(response.json())
