class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self, password):
        if password == "admin":
            print(self.salary)
        else:
            ("Invalid Access!!!")

    def set_salary(self, password, salary):
        if password == "admin":
            self.salary = salary
        else:
            ("Invalid Access!!!")

    def display_info(self):
        print(self.name, self.salary)

emp1 = Employee("Rahim", 20000)
emp1.display_info()
emp1.get_salary("admin")
emp1.set_salary("admin", 50000)
emp1.get_salary("admin")
emp1.display_info()
