# unordered
# immutable
# no duplicates
# set()
a = [1,1,2,2,3,4]
b = [2,3,4,5,6]
s = set(a)
print(s)
sb = set(b)
print(sb)

c = s.intersection(sb)
print(c)

c = s.union(sb)
print(c)