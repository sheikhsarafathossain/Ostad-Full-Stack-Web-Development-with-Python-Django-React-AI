# class Car:
#     def __init__(self, company_name, model, engine):
#         self.company_name = company_name
#         self.model = model
#         self.engine = engine

#     def printAll(self):
#         print(self.company_name)
#         print(self.model)
#         print(self.engine)


# c1 = Car("Toyota", "Corolla", "Petrol Engine")
# c1.printAll()

# class BankAccount:
#     def withdraw_money(self):
#         print("Money withdrawn!")

# class SavingsAccount(BankAccount):
#     pass

# class CurrentAccount(BankAccount):
#     pass

# b1 = BankAccount()
# b1.withdraw_money()

# b1 = SavingsAccount()
# b1.withdraw_money()

# b1 = CurrentAccount()
# b1.withdraw_money()


# class GrandFather:
#     def eye(self):
#         print("Red")

#     def lips(self):
#         print("hard")

# class Father(GrandFather):
#     def lips(self):
#         print("soft")

# class Mother:
#     def nose(self):
#         print("pointy")
#     def lips(self):
#         print("Hard")


# # MRO Method Resolution Order

# class Child(Father): #Multiple Inheritence
#     def lips(self):
#         super().lips()
# c1 = Child()
# c1.eye()
# c1.lips()


#Access Modifiers
class BankAccount:
    def __init__(self):
        self._name = "Mr A" # Protected
        self.balance = 12.0 # Public variable
        self.__pin = 1234 # Private


ba = BankAccount()
print(ba.balance)
print(ba._name)
print(ba._BankAccount__pin) # name Mangling
