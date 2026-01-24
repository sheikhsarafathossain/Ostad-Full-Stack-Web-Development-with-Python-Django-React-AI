import json

data = {
    "name" : "Rahim",
    "age" : 30,
    "is_logged_in" : True,
}

json_strings = json.dumps(data, indent=4)
# Serialization : python to json
print(json_strings)
print(type(json_strings))

# Deserialization : json to python

data = '{"name" : "Rahim", "age" : 30, "is_logged_in" : true, "test" : null}'

python_dict = json.loads(data)

print(python_dict)
print(type(python_dict))
