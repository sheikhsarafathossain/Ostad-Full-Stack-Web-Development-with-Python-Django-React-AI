class Car:
    def driver(self):
        return "Driving a car"
class Bike:
    def driver(self):
        return "Riding a bike"

class VehicleFactory:
    @staticmethod
    def get_vehicle(type):
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            return ValueError("Unknown Vehicle")

vehicle = VehicleFactory.get_vehicle("bike")
print(vehicle.driver())