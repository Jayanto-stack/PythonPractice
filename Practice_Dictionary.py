"""
Question 1:
Rivers: Make a dictionary containing three major rivers and the country 
each river runs through  One key-value pair might be 'nile': 'egypt' 
• Use a loop to print a sentence about each river, such as The Nile runs 
through Egypt 
• Use a loop to print the name of each river included in the dictionary 
• Use a loop to print the name of each country included in the dictionary 
"""
"""
rivers = {
    "nile": "egypt",
    "ganges": "india",
    "amazon": "brazil"
}
"""
# Print a sentence about each river
"""
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
"""
# Print the name of each river
"""
print("\nRivers:")
for river in rivers:
    print(river.title())
"""
# Print the name of each country
"""
print("\nCountries:")
for country in rivers.values():
    print(country.title())
"""
"""
Question 2:

Create a dictionary containing the name of five students and their marks.
Use for loop to print each student's name and marks.
Use a loop to print only the student names.
Use a loop to print only the marks.
Calculate and print the total marks of all five students.
"""
students = {
    "Rahul": 85,
    "Sanju": 67,
    "Aman": 85,
    "Neha": 75,
    "Rohan": 65
}
# Print each students names and marks
for names, marks in students.items():
    print(f"{names.title()} scored {marks} marks.")

# Print only the students name
print("\nStudents Names:")
for name in students:
    print(name)

# Print only the marks of students
print("\nStudents Marks:")
for marks in students.values():
    print(marks)

# Calculate total marks
total = 0
for marks in students.values():
    total += marks

print("\nTotal Marks:", total)

