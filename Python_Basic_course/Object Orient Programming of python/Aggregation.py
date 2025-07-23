# has a relationship

# a uni has departments

class dept:
    def __init__(self, name):
        self.name = name

class uni:
    def __init__(self, name):
        self.name = name  
        self.dept = []

    def add_dept(self, department):
        self.dept.append(department)  

    def show_dept(self):
        return [dept.name for dept in self.department]

un1 = uni("ABC")
dept1 = dept("Programming")
dept2 = dept("Math")

un1.add_dept(dept1)
un1.add_dept(dept2)
un1.show_dept()

