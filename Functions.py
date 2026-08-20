# What is a Function ?
"""
A function is a reusable block of code that performs a particular task.
Think of it like a machine.
"""
# Why do we need function ?
# Suppose you need to calculate the average of marks several times
# Without using function
"""
total = 80 + 70 + 56
average = total/3
print(average)
"""
"""
def greet():
    print("Hello!")
greet()
"""
"""
def welcome():
    print("Welcome to Python class!")
welcome()
welcome()
welcome()
"""
# Arguments and parameters
"""
def greet(name):
    print(f"Hello {name}!")
greet("Rahul")
greet("Sonu")
"""
"""
Parameter = variable written when defining the function
Argument = actual value given when calling the function
"""
# Why do we pass arguments
"""
def greet_rahul():
    print("Hello Rahul")
def greet_priya():
    print("Hello Priya")

greet_rahul()
greet_priya()
"""
"""
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total += number
print(total)
"""
"""
def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)

calculate_total([10, 20, 30, 40, 50, 60])
"""
# Return 
"""
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
"""
# Positional Argument
"""
def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'dobby')
describe_pet('hamster', 'harry')
"""
# Keyword Arguments
def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')

