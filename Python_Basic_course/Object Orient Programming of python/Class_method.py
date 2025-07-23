class Employee:
    company_name = "Rahi's Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayinfo(self):
        print(f"Employee name: {self.name} \n Emp salary: {self.salary}")    

    @classmethod
    def change_company_name(cls, name):
        cls.company_name = name    
          

obj1 = Employee("Rahi", 40000)
obj2 = Employee("Emon", 25000)   

obj1.displayinfo()
obj2.displayinfo()

Employee.change_company_name("Harvard company")

print(obj1.company_name)
print(obj2.company_name)