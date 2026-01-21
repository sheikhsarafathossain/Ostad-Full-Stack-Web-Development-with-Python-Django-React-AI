import requests
import json

res = requests.get("https://jsonplaceholder.typicode.com/posts")
print(res)

data = json.loads(res.text)

print(type(data[0]))