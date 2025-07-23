class grandfather:
    def __init__(self, name , color):
        self.name = name
        self.color = color

class father(grandfather):
    def __init__(self, hobby, name, color):        
        super().__init__(name, color)
        self.hobby = hobby

gf1 = grandfather("Chowdhury", "red")
f1 = father('Football', "chowdhury", "red")

print(f1.color)
