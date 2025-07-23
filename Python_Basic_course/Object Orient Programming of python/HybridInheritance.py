class shape:
    def area(self):
        print("this area is......")

class polygon(shape):
    def sides(self):
        print("This thing has four sides.....")

class rectangle(polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

rec = rectangle(10, 5)
rec.sides()
print(rec.area())    
   