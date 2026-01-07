import functools
import math

square = lambda x,y: x*y

print(square(2,2))
# map
nums = [1,2,3,4]
square_number = list(map(lambda x: x**2,nums))
print(square_number)

# sorting
students = [("Rahim", 60), ("Karin", 33), ("Sarafat", 44)]
sort_std = sorted(students, key=lambda x: x[1])
print(sort_std)

# Filter 

even = list(filter(lambda x: x%2 == 0, nums))
print(even)


# reduce
# reduce need functools package
# import functools

sum = functools.reduce(lambda x,y : x+y, nums)
print(sum)


# other way to do it
cal = int(math.fsum(nums))
print(cal)