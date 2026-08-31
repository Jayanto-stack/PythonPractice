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
