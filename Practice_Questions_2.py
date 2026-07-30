"""
Question 1:
Write a Python program that:
1. Takes the student's name as input.
2. Takes marks for 3 subjects as input.
3. Calculates the total marks and average.
4. Display the grade using the following criteria:
    90 and above --> A
    75 to 89     --> B
    60 to 74     --> C
    40 to 59     --> D
    Below 40     --> F

Sample Output:
Enter student name: Rahul
Enter marks of Subject 1: 80
Enter marks of Subject 2: 75
Enter marks of Subject 3: 90

Student Name: Rahul
Total Marks : 245
Average     : 81.67
Grade       : B
"""
"""
name = input("Enter student name :")
subject_1 = int(input("Enter marks of Subject 1 :"))
subject_2 = int(input("Enter marks of Subject 2 :"))
subject_3 = int(input("Enter marks of Subject 3 :"))

print("Student Name:", name)

total = (subject_1 + subject_2 + subject_3)
print("Total Marks:", total)

average = total/3
print("Average:", average)

if average >= 90:
    print("Grade : A")
elif average >= 75:
    print("Grade : B")
elif average >= 60:
    print("Grade : C")
elif average >= 40:
    print("Grade : D")
else:
    print("Grade : F") 
"""
"""
Question 2
Create a list containing the prices of five shopping items.
1. Calculate the total bill using a for loop.
2. If the total bill is £500 or more, give a 10% discount.
3. Otherwise, no discount is applied.
4. Print:
	Original Bill
	Discount
	Final Bill

Sample Output:

Shopping Prices: [120, 250, 180, 150, 100]
Original Bill : 800
Discount      : 80.0
Final Bill    : 720.0
"""
"""
prices = [120, 50, 100, 200, 250]
total = 0
for price in prices:
    total += price

if total >= 500:
    discount = total*10/100
else:
    discount = 0

final_bill = total - discount
print("Shopping Prices :", prices)
print("Original Bill :", total)
print("Discount :", discount)
print("Final Bill :", final_bill)
"""
"""
Question 3
Write a program that:
1. Accepts 10 numbers from the user.
2. Stores them in a list.
3. Uses a for loop to count:
	Even numbers
	Odd numbers
4. Print:
	List of numbers
	Total even numbers
	Total odd numbers

Sample Output:
Enter Number 1: 5
Enter Number 2: 8
...
Enter Number 10: 17

Numbers: [5, 8, 12, 7, 15, 20, 11, 18, 6, 17]

Even Numbers : 5
Odd Numbers  : 5
"""
numbers = []

for i in range(10):
    number = int(input(f"Enter Number {i}:"))
    numbers.append(number)
even = 0
odd = 0

for number in numbers:
    if number %2 == 0:
        even += 1
    else:
        odd += 1
print("\nNumbers :", numbers)
print("Even Numbers :", even)
print("Odd Numbers :", odd)

