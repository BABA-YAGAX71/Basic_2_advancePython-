class lptop:
    def __init__(self, brand):
        self.brand = brand

class stu:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.lptp = laptop_obj

    def show_laptop_info(self):
        print(f"{self.name} has a laptop named {self.lptp.brand}")   

lp1 = lptop("Asus")
student = stu("rahim", lp1)
student.show_laptop_info()