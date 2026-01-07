a = {
    "rahim" : 12,
    "karim" : 14,
    "fahim" : [1,2,3,4]
}

print(a)
print(type(a))

for i in a:
    print(i)

for i in a.values():
    print(i)
print(a.keys(), a.values())

for k,v in a.items():
    print(f"Key Name : {k}, Values : {v}")

print("----------")

a = [1,2,3]
b = ["one", "two", "three"]
c = dict(zip(a,b))
print(c)
print(c[1])


print(zip(a,b))
print(list(zip(a,b)))
print(tuple(zip(a,b)))

print(set(zip(a,b)))