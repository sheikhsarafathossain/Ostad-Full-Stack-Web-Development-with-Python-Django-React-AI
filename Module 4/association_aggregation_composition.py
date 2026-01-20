# Association

# Student, Laptop 
# 2 class interaction 

class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Student:
    def __init__(self,name, laptop):
        self.name = name
        self.laptop = laptop
    
    def show_laptop_info(self):
        print(f"{self.name} has a laptop named: {self.laptop.brand}")

l1 = Laptop("Toshiba")

std1 = Student("Sarafat",l1)
std1.show_laptop_info()

# Aggregation

# Combination of multiple object
# Has-A Relationship

class Department:
    def __init__(self,name):
        self.name = name

class University:
    def __init__(self,name):
        self.name = name
        self.departments = []
    def add_department(self, department):
        self.departments.append(department)

    def show_departments(self):
        return [department.name for department in self.departments]

dp1 = Department("CSE")
dp2 = Department("EEE")
un1 = University("ABC")
un1.add_department(dp1)
un1.add_department(dp2)
print(un1.show_departments())


# Composition
# Car, engine Strong Relationship

class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)

    def show_details(self):
        print(self.brand)
        print(self.engine.power)
c1 = Car("Toyota", 500)
c1.show_details()