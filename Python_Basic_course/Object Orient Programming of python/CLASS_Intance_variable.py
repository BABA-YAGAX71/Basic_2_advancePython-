class school:
    school_name = "Ostad high school"

    def __init__(self, name):
        self.students = name

sc1 = school("Rahim")
print(sc1.school_name)
print(sc1.students)