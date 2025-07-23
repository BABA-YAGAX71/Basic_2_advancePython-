class Car:
    def driver(self):
        return "driving car safe"
    
class Bike:
    def driver(self):
        return "riding a bike"


class vehicleFactory:
    @staticmethod
    def get_vehicle(type):
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            return ValueError("Unknown vehicle")
        

ob1 = vehicleFactory.get_vehicle("car") 
print(ob1.driver())       


