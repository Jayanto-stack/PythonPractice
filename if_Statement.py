"""
cars = ['audi', 'bmw', 'toyota', 'mercedes']
for car in cars:
    if car == 'suzuki':
        print(car.upper())
    else:
        print(car.title())
"""
"""
students = []
for student in students:
    if student == '':
        print()
    else:
        print()
"""
"""
age = 14
if age >= 18:
    print("You're old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
"""
"""
1. Admission for anyone under age 4 is free.
2. Admission for anyone between the age of 4 and 18 is $10.
3. Admission for anyone age 18 or older is $15.
"""
"""
age = 2
if age < 4:
    print("Your admission is free")
elif age < 18:
    print("Your admission cost is $10.")
else:
    print("Your admission cost is $15.")
"""
"""
marks = int(input("Enter the marks :"))
if marks > 85 and marks <= 100:
    print("Congrats! you have scored grade A.")
elif marks > 60 and marks <= 85:
    print("You have scored B+..")
elif marks > 40 and marks <= 60:
    print("You have scored B ..")
elif marks >30 and marks <= 40:
    print("You have score C ..")
else:
    print("Sorry you are fail?")
"""
"""
Enter a value: 10
Enter b value: 20
Enter c value: 5
Maximum value is: 20
"""
"""
a = int(input("Enter a value :"))
b = int(input("Enter b value :"))
c = int(input("Enter c value :"))
if (a>b) and (a>c):
    print("Maximum value is:", a)
elif (b>c):
    print("Maximum value is:", b)
else:
    print("Maximum value is:", c)
"""
number = -5
if number > 0:
    print("It's a Postive number")
elif number < 0:
    print("It's a Negative number")
else:
    print("It's a Zero")
