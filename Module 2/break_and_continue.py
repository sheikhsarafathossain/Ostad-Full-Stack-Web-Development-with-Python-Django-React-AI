a = [1,2,3,4,'a',5,6,7]

for i in a:
    if type(i) == str:
        break
    else:
        print(i)

for i in a:
    if type(i) == str:
        continue
    else:
        print(i)