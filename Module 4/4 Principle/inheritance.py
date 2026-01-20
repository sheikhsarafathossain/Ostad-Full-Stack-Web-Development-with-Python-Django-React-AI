# Single Inheritance
# Multi Inheritance
# Multi Level Inheritance
# Hierarctical Inheritance
# Hybrid Inheritance

class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
    def gf_method(self):
        print("GrandFather")

class Father(GrandFather):
    def __init__(self, hobby):
        # GrandFather.__init__(color, first_name)
        self.hobby = hobby
    # def __init__(self, color, first_name):
    #     super().__init__(color, first_name)
    def f_method(self):
        print("Father")
    
class Children(Father,GrandFather):
    def __init__(self, color, first_name, hobby, fashion):
        Father.__init__(self,hobby)
        GrandFather.__init__(self,color,first_name)
        self.fashion = fashion
# gf1 = GrandFather("Red", "Sheikh")
# f1 = Father("red","Chowdhury","Cricket")
# print(f1.color)
# print(f1.hobby)


c1 = Children("Red", "Sheikh", "Cricket", "Modern")
c1.gf_method()
c1.f_method()
print(c1.fashion)
print(c1.first_name)
print(c1.hobby)

# Hierarctical Inheritance


class Vehicle:
    def engine_type(self):
        print("Vehicle has and engine")

class Car(Vehicle):
    def nums_doors(self):
        print("Car has 4 doors")
class Truck(Vehicle):
    def load_capacity(self):
        print("Truck can carry 10 tons")

car  = Car()
car.engine_type()
car.nums_doors()

truck = Truck()
truck.engine_type()
truck.load_capacity()

# Hybrid Inheritance

class Shape:
    def area(self):
        print("Calculating Area...")
class Polygon(Shape):
    def sides(self):
        print("Polygon has multiple sides.")
class Rectange(Polygon):
    def __init__(self, length, bredth):
        self.length = length
        self.bredth = bredth

    def area(self):
        return self.bredth*self.length

red = Rectange(10,5)
red.sides()
print(red.area())
red.area()