# 3 types of constructor

'''
1. Default constructor
2. parameterized constructor

3. Default value constructor'''


# class and Obj creation
# what we have made in the class is called method usually we call it function

class car:
    '''def __init__(self): #1. Default constructor
        self.brand = ""
        self.model = ""'''
    '''def __init__(self, brand, model):  #2. parameterized constructor
        self.brand = brand
        self.model = model'''   
    def __init__(self, brand="Toyota", model = "Gazo"):  # 3. Default value constructor
        self.brand = brand
        self.model = model  
'''
car1 = car() #Object
car1.model = "Corolla"
car1.brand = "Honda"

print(car1.brand)
print(car1.model)'''

'''car2 = car("Toyota", "Civic")
print(car2.brand)
print(car2.model)'''

car3 = car()
print(car3.brand)
print(car3.model)

