# Composition

# car, engine

class Engine:
    def __init__(self, power):
        self.power = power

class car:
    def __init__(self,brand, power):
        self.brand = brand
        self.engine = Engine(power)

    def  show(self):
        print(f"{self.brand} has an engine with {self.engine.power} HP")

car1 = car("Tyota", 100)
car1.show()      

