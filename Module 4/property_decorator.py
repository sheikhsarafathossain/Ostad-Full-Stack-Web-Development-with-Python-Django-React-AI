class Employee:
    company_name = "Ostad Company"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property # make read only no setter allow
    def salary(self):
        return self._salary
    @salary.setter # making setter
    def salary(self,salary):
        self._salary = salary


ob1 = Employee("rahhhim", 4000)

print(ob1._salary)
print(ob1.salary)
# ob1._salary = 7000
# print(ob1._salary)

ob1.salary = 6000
print(ob1._salary)
print(ob1.salary)