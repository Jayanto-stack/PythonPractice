"""
Question 1:
Create a program that:
- Creates a list of 5 subject marks.
- Uses a for loop to calculate the total marks.
- Calculates the average marks.
- Prints:
	Total marks
	Average marks

Sample Output:
Subject Marks: [75, 82, 90, 68, 85]
Total Marks: 400
Average Marks: 80.0
"""
marks = [75, 82, 90, 68, 85]

# Variable to be store total marks
total = 0

for mark in marks:
    total += mark

# Calculate the average marks
average = total/len(marks)

# Display Output
print("Subject Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)

"""
Question 2:
1. Create a list of your 5 favorite movies.
2. Use a for loop to print an invitation-style message for each movie.

Sample Output:
I would like to watch Avengers today.
I would like to watch Interstellar today.
I would like to watch Inception today.
I would like to watch The Dark Knight today.
I would like to watch Titanic today.
"""
movies = [
    "Avengers",
    "Interstellar",
    "Inception",
    "The Dark Knight",
    "Titanic"
]
for movie in movies:
    print(f"I would like to watch {movie} today.")
"""A customer bought the following items:
120
250
80
150
300
1. Store the prices in a list.
2. Use a for loop to calculate the total bill.
3. Add 18% GST to the bill.
4. Print:
	Original Bill
	GST Amount
	Final Bill

Sample Output:
Original Bill : 900
GST (18%)     : 162.0
Final Bill    : 1062.0
"""
prices = [120, 250, 80, 150, 300]
bill = 0
for price in prices:
    bill += price

# Calculate GST
gst = bill * 18 / 100
# Final Bill
final_bill = bill + gst
# Display Output
print("Original Bill:", bill)
print("GST (18%):", gst)
print("Final Bill:", final_bill)

"""
Question 4:
Create a list of 6 student names.
Use a for loop to print the attendance like this:
Roll No. 1 : Rahul
Roll No. 2 : Priya
Roll No. 3 : Aman

(Hint: You may use a separate variable to keep track of the roll number.)

Sample Output:
Roll No. 1 : Rahul
Roll No. 2 : Priya
Roll No. 3 : Aman
Roll No. 4 : Neha
Roll No. 5 : Rohan
Roll No. 6 : Simran
"""
students = [
    "Rahul",
    "Priya",
    "Aman",
    "Neha",
    "Rohan",
    "Simran",
]
roll = 1
for student in students:
    print(f"Roll No.{roll}: {student}")
    roll += 1

