
"""
Docstring for Module 3.file_handling


r -> Open file for Reading
w -> Open file for Writing
a -> Open file Reading for writing 
    (writers at the end) if not exist
    create new


"""


# f = open("textbook.txt","r")
# data = f.read()
# f.seek(0)
# print(f.read())
# f.close()

# print(data)

with open("textbook.txt", "r") as f:
    content = f.read() # read(5) show 5 char
    print(content)

#write -> delete old file values
with open("textbook.txt", "w") as f:
    f.write("Hello world\n")
    f.write("I am writing in a file \n")
    print(content)

#append -> add at last of the file values
with open("textbook.txt", "a") as f:
    f.write("Hello world\n")
    f.write("I am writing in a file \n")
    print(content)

lines = ["I Love Python\n","I am new to python\n"]

with open("textbook.txt", "a") as f:
    f.writelines(lines)

"""

Mystery of path

Path is where a file / folder resides

two types of path:
1. Absolute path (starts from os/drive root)
    E:\code\hobby\text.txt
2. Relative path (start from current directory)
    text.txt
    ..\module 2/text.txt

"""



