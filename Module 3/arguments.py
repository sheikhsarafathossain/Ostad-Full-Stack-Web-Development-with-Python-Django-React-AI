def addition(*args):
    print(args)    
    result = sum(args)
    return result

r = addition(10,20,30)
print(r)