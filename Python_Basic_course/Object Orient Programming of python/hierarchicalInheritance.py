class vehicle:
    def enginetype(self):
        print("Hino 1j")

class car(vehicle):
    def Cartype(self):
        print("Its a Bus")

class bus(car):
    def passenger(self):
        print("there are 36 seats")

car = car()  
bus = bus()    

car.Cartype()
car.enginetype()
bus.passenger()
        