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
"""
def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
"""
# Return 
"""
def get_formatted_name(first_name, last_name, middle_name=''):
    # Return a full name, neatly formatted.
    if middle_name:
        full_name = first_name + ' ' + middle_name +' '+ last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('lata', 'mangeshkar')
print(musician)
musician = get_formatted_name('rahat', 'ali khan', 'fateh')
print(musician)
"""
# Return a dictionary
"""
def build_person(first_name, last_name):
    # Return a dictionary of information about a person
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('Arjit', 'Singh')
print(musician)
"""
