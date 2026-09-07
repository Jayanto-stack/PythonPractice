'''
The four Pillars of OOPs in Python
- Encapsulation:- Putting pieces in a labelled box so nobody messes with them randomly
- Abstraction:- giving someone a "steering wheel" instead of the whole engine.
- Inheritance:- Reusing an existing LEGO set's design to build a bigger set.
- Polymorphism:- When the same instruction ("build a wheel") works differently depending on which set you're using.
'''
'''
Encapsulation:
Bundle data(variables) and the methods that work on that data into a single unit (a class), and restrict
direct access to some of that data from outside the class.
'''
'''
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}. New balance:{self.__balance}")
        else:
            print("Invalid or insuffcient funds.")

    def get_balance(self):
        return self.__balance

account = BankAccount("Jayanto", 10000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
# print(account.__balance)  # This will provide a attribute Error
'''
'''
Create a class Student with a private attribute __marks() that only allows values between 0 and 100
and a method get_marks() to retrieve it.
'''
class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):
        if 0 <= marks <=100:
            self.__marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

    def get_marks(self):
        return self.__marks

s = Student("Riya")
s.set_marks(85)
print(s.get_marks())
s.set_marks(150)
print(s.get_marks())        
