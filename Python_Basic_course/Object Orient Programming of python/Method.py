class car:

    def __init__(self, brand="Toyota", model = "Gazo"):  # 3. Default value constructor
        self.brand = brand
        self.model = model  

    def display_info(self):
        print(f"Brand = {self.brand}, Model = {self.model}")


car1 = car() #Object

print(car1.brand)
print(car1.model)