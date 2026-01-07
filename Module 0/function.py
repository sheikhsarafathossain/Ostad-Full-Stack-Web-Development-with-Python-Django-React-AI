def validation(**kwargs):
    print(kwargs)
    if(kwargs['name']=="Sarafat" and kwargs["dept"]=="CSE"):
        print(f"Welcome {kwargs["id"]}")
    else:
        print("Not CSE Student")

name = input("Enter your name: ")
dept = input("Enter your dept: ")
id = input("Enter your id: ")

validation(name = name,dept = dept,id = id)