# Scope -> a region where a variable is accessible

x = 10 # Global Variable

def func():
    y = 19
    x = 200
    print(x, y)
    

func()
# print(y)
print(x)

# LEGB => Local Enclosing Global Block

# n = "Global" # Global

# def outer():
#     n = "Enclosing" # Enclosing Variable
#     def inner():
#         n = "Local" # Local Variable

#         print(n)
#     inner()
# outer()
# print(n)


n = "Global" # Global

def outer():
    n = "Enclosing" # Enclosing Variable
    def inner():
        global n # imp
        n = "Local" # Local Variable
        
        print(n)
    inner()
    print(n)
outer()
print(n)

print("-------")
n = "Global" # Global

def outer():
    n = "Enclosing" # Enclosing Variable
    def inner():
        nonlocal n # imp
        n = "Local" # Local Variable
        
        print(n)
    inner()
    print(n)
outer()
print(n)