class grandfather:
    print("grandfather says.....")

class father(grandfather):
    def greet(self):        
        print("Father says.........")

class children(father):
    def greet(self):
        print("children says.......")

gf = grandfather()
fath = father()
chil = children()

fath.greet()
chil.greet()