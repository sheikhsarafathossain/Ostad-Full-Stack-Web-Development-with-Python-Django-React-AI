class Employee:
    company_name = "Abc Company"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self): # instance method
        print(f"Company Name:  {self.company_name}")
        print(f"Employee name: {self.name}\n {self.salary}")
    
    @classmethod
    def change_company_name(cls, name): #Class Method
        cls.company_name = name

ob1 = Employee("rahim", 30000)

ob1.display_info() # calling instance method

Employee.change_company_name("XYZ Company") # calling class method

ob1.display_info()

ob2 = Employee("Kahim", 30000)
ob2.display_info()