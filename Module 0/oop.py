class Car:
    def __init__(self):
        self.brand = ""
        self.model = ""

    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def __init__(self, brand="Toyota", model="Coroal"):
        self.brand = brand
        self.model = model

    def carmodel(self):
        print("Sar")


car3 = Car("Honda", "civic")
print(car3.brand)

car1 = Car()
print(car1.brand)
car1.carmodel()