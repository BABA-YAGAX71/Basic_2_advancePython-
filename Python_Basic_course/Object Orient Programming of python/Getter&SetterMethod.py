class employee:
    company_name = "ostad"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self, password):
        if password == "admin":
            print(self._salary)
        else:
            print("Invalid Access!!!")        
    def set_salary(self, password, salary):
        if password == "admin":
            self._salary = salary
            print(f"New Salary : {self._salary}")
        else:
            print("Invalid Access!!!")
ob1 = employee("rahi", 40000)
ob2 = employee("Emon", 200)

ob1._salary = 6000

print(ob1._salary)
print(ob2.set_salary("admin", 7000))
        