class Car:
    def __init__(self, company_name, model, engine):
        self.company_name = company_name
        self.model = model
        self.engine = engine

    def printAll(self):
        print(self.company_name)
        print(self.model)
        print(self.engine)


c1 = Car("Toyota", "Corolla", "Petrol Engine")
c1.printAll()

class BankAccount:
    def withdraw_money(self):
        print("Money withdrawn!")

b1 = BankAccount()
b1.withdraw_money()
