a = [1,2,3,4,5]


result = []

#normal way

for i in a:
    if i%2==0:
        result.append(i)

print(result)

# List comprehension

new_result = [i for i in a if i%2==0]
print(new_result)

b_new = [i**2 if i%2==0 else i for i in a]
print(b_new)