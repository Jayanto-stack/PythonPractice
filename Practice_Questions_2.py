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
Question 2:

"""