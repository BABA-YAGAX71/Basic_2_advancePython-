class grandfather:
    def __init__(self, name , color):
        self.name = name
        self.color = color
    def g_f_method(self):
        print("I am from grandFather")

class father(grandfather):
    def __init__(self, hobby, name, color):        
        super().__init__(name, color)
        self.hobby = hobby
    def Father_method(self):
        print("i am from father")

class children(father, grandfather):
    def __init__(self, fashion):
        self.fashion = fashion

gf1 = grandfather("Chowdhury", "red")
f1 = father('Football', "chowdhury", "red")

c1 = children("test")
print(c1.fashion)

print(f1.color)
