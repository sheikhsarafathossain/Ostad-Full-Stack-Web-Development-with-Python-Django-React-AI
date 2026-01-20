# poly --> multi
# morphism --> form

# 1. Method Overriding


class GrandFather:
    def greet(self):
        print("Grandfather says")
class Father(GrandFather):
    def greet(self):
        print("Father says")
class Children(Father):
    def greet(self):
        print("Children says")

gf = GrandFather()
gf.greet()

f = Father()
f.greet()

c = Children()
c.greet()

# 2. Method Overloading

class Shape:
    def area(self):
        return 10
    def area(self, a,b):
        return a*b

p = Shape()
print(p.area())