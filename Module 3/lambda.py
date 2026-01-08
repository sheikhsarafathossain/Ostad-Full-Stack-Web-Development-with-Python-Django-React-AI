import functools
# Anonymous function -> Unnamed function
# cannot use print
# Only return value


def sqr(x):
    return x*x

print(sqr(2))

square = lambda x: x*x
print(square(4))

students = [("Rahim", 60), ("Karim",49), ("Fahim", 100)]
sorted_student = sorted(students,key=lambda x: x[1])

print(sorted_student)


"""
map(logic, data_set), filter(logic, data_set), reduce(logic, data_set)


import functools -> to use reduce
"""
# Map
nums = [1,2,3,4]
sr_nums = list(map(lambda x: x*x,nums))
print(sr_nums)
even = list(map(lambda x: x%2 == 0, nums))
print(even)


# Filter
even = list(filter(lambda x: x%2 == 0, nums))
print(even)

# reduce
sum = functools.reduce(lambda x,y: x+y, nums)
print(sum)