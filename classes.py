'''
Classes annd Objects
Class: Class is a blue print for creating objects. Example: Car manufacturing

Constructor:
All classes have a function called __init__(), which is always executed when the object
is being initiated.
Creating Class syntax:
class student:
    def __init__(self, fullname):
        self.name = fullname
# The self parameter is a refernece to the current instance of the class, and is used to access variables that belong
# to the class.

Creating Object syntax:
s1 = student("karan")
print(s1.name)
'''
'''
class student:
    # name = "karan"
    def __init__(self, fullname):
        self.name = fullname
        print("adding a student in a database.")

s1 = student("Karan")
print(s1)
'''
'''
class Student:
    def __init__(self, fullname):
        self.name = fullname        # Instance Attribute
        print("Adding students in a database")

s1 = Student("karan")
print(s1.name.title())

s2 = Student("Varun")
print(s2.name)
'''
'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database")

    def welcome(self):
        print("Welcome students.")

    def get_marks(self):
        return self.marks
'''
'''
Methods:
Methods are functions that belong to objects.
'''
'''
s1 = Student("Karan", 90)
s1.welcome()
print(s1.get_marks())
print(s1.name, s1.marks)

s2 = Student("Raju", 78)
s2.welcome()
print(s2.name, s2.marks)
'''
# Create student class that takes name & marks of 3 subjects as agruments in constructor. Then create a method
# to print the average.
'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name.title(), "you have scored:", self.marks, "and your avg score is:", sum/3)

s1 = Student("fanendra", [70, 65, 80])
s1.get_avg()

s2 = Student("jay", [70, 55, 39])
s2.get_avg()
'''
'''
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' '+ self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
'''
class Dog():
    """A simple attempt to model a DOG. """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('hunter', 5)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is "+ str(my_dog.age) + " years old.")
print(my_dog.sit())

my_second_dog = Dog('bruno', 3)
print(my_second_dog.roll_over())