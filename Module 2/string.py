name = "Sheikh Sarafat Hossain"
print(name)

# print(name[0])

# name[0] = "R"
# print(name[0])
print(name.capitalize())
print(name.casefold())
print(name.center(1))
print(name.center(50," ")) 
print(name.count("n",0,len(name)))
txt = "Hello, welcome to my word."

x = txt.endswith(("world.", "castle.","word."))

print(x)

txt = "Hello, welcome to my world."

print(txt.find("w"))
print(txt.index("w"))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1,txt2,txt3)

myvar = {"name" : "Jane", "age" : 36}
txt = "Happy birthday {name} you are now on level {age}!"
print(txt.format_map(myvar))

txt = "123"

x = txt.isalnum()

print(x)

txt = "Company10"

x = txt.isalpha()

print(x)

txt = "1234"

x = txt.isdecimal()

print(x)

txt = "50800"

x = txt.isdigit()

print(x)

txt = "hello world!"

x = txt.islower()

print(x)

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())


a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)

txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

txt = "Welcome to my world"

x = txt.title()

print(x)


txt = "Hello my friends"

x = txt.upper()

print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(20))
print(b.zfill(10))
print(c.zfill(10))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)
txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)