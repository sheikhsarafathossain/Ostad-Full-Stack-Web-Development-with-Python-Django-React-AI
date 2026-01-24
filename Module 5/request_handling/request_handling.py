# System

# Request, Response Cycle

# POST GET PUT/PATCH DELETE

import requests
# GET Request
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.json())

# POST request
print("----------")
data = {'userId': 5, 'id': 48, 'title': 'ut voluptatem illum ea doloribus itaque eos', 'body': 'voluptates quo voluptatem facilis iure occaecati\nvel assumenda rerum officia et\nillum perspiciatis ab deleniti\nlaudantium repellat ad ut et autem reprehenderit'}
response = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
print(response.status_code)
print(response.json())


# UPDATE request
print("----------")
data = {'userId': 5, 'id': 48, 'title': 'for test(updated)'}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1",json=data)
print(response.status_code)
print(response.json())

# Delete request
print("----------")
# data = {'userId': 5, 'id': 48, 'title': 'for test(updated)'}
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())