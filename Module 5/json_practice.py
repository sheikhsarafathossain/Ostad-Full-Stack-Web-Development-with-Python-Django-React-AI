import json
import datetime
student = {
    "name" : "Sarafat",
    "Roll" : "01",
    "Marks" : [100,100,100],
    "TimeStamp" : datetime.datetime.now().strftime("%B %d, %Y")
}

print(type(student))

st_text = str(student)
print(st_text)

st_text = json.dumps(student)
print(repr(st_text)) # text er representation

ob = json.loads(st_text)
print(ob)
print(ob["name"])
print(type(ob["Name"]))