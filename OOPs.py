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
'''
'''
Abstraction
Means hiding unnecessary implementation details and showing only what the user need to use.
'''
'''
class Car:
    def start(self):
        self.__check_engine()
        self.__inject_fuel()
        self.__start_engine()
        print("Car started")

    def __check_engine(self):
        print("Checking engine...")

    def __inject_fuel(self):
        print("Injecting fuel...")

    def __start_engine(self):
        print("Starting engine...")

car = Car()
car.start()
'''
# abc module = Abstract Base Classes 
# Payment System
'''
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass                # No implementation here -- 

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

def checkout(payment_method: Payment, amount):
    payment_method.pay(amount)

checkout(CreditCardPayment(), 5000)
checkout(UpiPayment(), 1000)
'''
'''
The checkout() function doesn't need to know the internal logic of each parameter type 
- it just calls .pay()
'''

'''
Create an Employee class by defining employee attributes such as name and salary as an instance
variable and implementing behavior using work() and show() instance method.
'''
'''
class Employee:
    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project

    def show(self):
        print("Name: ", self.name) 
        print("Salary: ", self.salary)

    def work(self):
        print(self.name, 'is working on', self.project)

emp = Employee('Jayanto', 80000, 'IT')
emp.show()
emp.work()
'''
'''
class Mobile:
    def __init__(self, brand, battery):
        self.brand = brand
        self.__battery = battery

    def charge(self, amount):
         self.__battery = self.__battery + amount
         if self.__battery > 100:
              self.__battery = 100
    def show_battery(self):
        print("Brand:", self.brand)
        print("Battery:", self.__battery, "%")

mobile = Mobile("Samsung", 60)
mobile.show_battery()
mobile.charge(30)
mobile.show_battery()
mobile.charge(50)
mobile.show_battery()
'''
# Inheritance
'''
A class (child/derived class) can axquire the properties and methods of another class (parents/base class), 
so you don't have to rewrite common logic.
'''
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

dog = Dog("Hunter")
cat = Cat("Billo")

print("Dog Name:", dog.name)
print("Sound:", end=" ")
dog.make_sound()
print()

print("Cat Name:", cat.name)
print("Sound:", end=" ")
cat.make_sound()
'''

'''
Create a Python program for a school.
	• Create a parent class called Person. 
	• Give it an attribute called name. 
	• Create a method called introduce() that prints the person's name. 
	• Create a child class called Student. 
	• Student should inherit from Person. 
	• Add a method called study() to the Student class. 
    - Create a Student object and call both methods.
'''
'''
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

class Student(Person):

    def study(self):
        print(self.name, "is studying.")

student = Student("Jayanto")
student.introduce()
student.study()
'''
# Polymorphism
'''
The same method name behaves differently depending on the object calling it. 
"Poly" = many
"morph" = forms
Think it like starting any object like, start a car, start a computer, start a conversation.
'''
'''
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implemented")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.speak())
'''
'''
Question of Polymorphism:
Write a function total_cost(items) that works for a list of objects, 
each having their own .price() method (e.g., Book, Electronics), and returns the total combined price 
'''
class Book:
    def __init__(self, title, price):
        self.title = title
        self._price = price

    def price(self):
        return self._price

class Electronics:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def price(self):
        return self._price

def total_cost(items):
    return sum(item.price() for item in items)

cart = [Book("Python 101", 400), Electronics("Headphones", 800)]
print(f"Total: {round(total_cost(cart), 2)}")
