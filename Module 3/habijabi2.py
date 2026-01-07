# Syntax Error
# if True print("Hello")


# Name Error
# a = 5
# print(b)


# Type Error
# a = "a" + 10
# print(a)


# Value Error
# x = int("Abcd")
# print(x)


# Index Error
# fruits = ['Apple', 'Banana']
# print(fruits[5])


# Key Error
# std = {
#     "name" : "Sarafat"
# }

# print(std["age"])


# Zero Division Error
# print(123/0)


try:
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))

    print("Result ", a / b)

except ZeroDivisionError:
    print(f"Cannot be divided by {b}")

except ValueError:
    print("Enter Number only")

except:
    print("Unknown Error")