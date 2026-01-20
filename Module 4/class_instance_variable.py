class School:
    school_name = "Ostad high School" # Class Variable


    def __init__(self, name):
        self.student_name = name # instance Variable


sc1 = School("Rahim")
School.school_name = "test"
print(sc1.school_name)
sc1.school_name = "SSS"
print(sc1.school_name)
print(sc1.student_name)

sc2 = School("Korim")
print(sc2.school_name)
print(sc2.student_name)