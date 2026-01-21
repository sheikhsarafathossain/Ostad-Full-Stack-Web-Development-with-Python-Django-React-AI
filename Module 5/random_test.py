import random

# help(random)
# print(dir(random))

# print(random.__doc__)

print(random.random())
print(random.uniform(5,10))
print(random.randint(1,100))
print(random.randrange(1,100,5))

fruits = ["apple", "banana", "cherry"]

print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)


def generate_pin():
    return random.randint(1000,9999)

print(f"your 4 digit pin: {generate_pin()}")