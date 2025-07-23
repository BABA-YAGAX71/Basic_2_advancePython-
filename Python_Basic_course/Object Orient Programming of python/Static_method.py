class school:
    school_name  = "Abc School"

    @staticmethod
    def calculate_grade(marks):
        if marks >= 90:
            return 'A+'
        else:
            return 'F'
        
print(school.calculate_grade(94))        