file = open("names.txt", "r")
content = file.read()
print(content)

file.close()

 
with open("names.txt", "r") as f:
    content = f.read()
    print(content)

with open("names.txt","a") as f:
    f.write("\nTest\n")


with open("names.txt", "r") as f:
    content = f.read()
    print(content)