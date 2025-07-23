class grandfather:
    print("grandfather says.....")
    def __init__(self):
        self.name = "chowdhury" # public
        self._age = '39' #protected
        self.__bankbalance = '40000' #private

class father(grandfather):
    def greet(self):        
        print(f"Father says.........{self.__bankbalance}")

class children(father):
    def greet(self):
        print("children says.......")

gf = grandfather()
fath = father()
chil = children()

fath.greet()
chil.greet()

print(fath.__bankbalance)