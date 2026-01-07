import copy 


a = [1,2,3]
print(a)

print(a[0])
a[0] = 4    #list is mutable
print(a)

s = "Hello"


l = list(s)
l.append(" ")
l.append("l")
print(l)

ll = copy.deepcopy(l)
ll[0] = "l"
print(ll)

ll.sort(reverse=False)
print(ll)
ll.sort(reverse=True)
print(ll)

val = ll.pop(1)
print(val)
print(val)


ll.clear()
print(ll)

#tuples

t = (1,2,3)
# t[0] = 1
print(t)

tr = list(reversed(t))
print(tr)
tr = tuple(reversed(t))
print(tr)