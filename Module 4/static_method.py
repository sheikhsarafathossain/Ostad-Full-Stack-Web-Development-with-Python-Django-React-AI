class School:
    school_name = "ABC School"

    @staticmethod
    def calculate_grade(marks): # Helper Function, no self or cls
        if marks >= 90: # no class or instance needed
            return "A+"
        else:
            return "Fail"
        
print(School.calculate_grade(1))