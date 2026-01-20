class Car:
    def __init__(self):
        self.brand = ""  # Default Constructor
        self.model = ""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model #Parameterized Constractor

    def __init__(self, brand="Toyota", model="Civic"):
        self.brand = brand
        self.model = model #Default Value Constractor

    def display_info(self):
        print(self.brand) # method inside class
        print(self.model)

car1 = Car()
# car1.brand = "Toyota"
# car1.model = "Supra"

print(car1.brand)
print(car1.model)

car2 = Car("Honda", "Civic")
print(car2.brand)
print(car2.model)
# print(Car.brand)
# print(Car.model)

car3 = Car("BMW", "M3")
car3.display_info() # calling method inside class
