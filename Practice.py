# Practice Questions
# Topics include in the below practice Questions are variables, list, string

# Question 1
"""
1. Create a list with the name of three guests.
2. Print an invitation message for each guest.
3. Replace any Guest from list, and print the invitation message.
"""
# f-string ---> You can put expressions inside {}
"""
guest = ['ram', 'shayam', 'raju', 'jagdish']
guest[3] = "elon musk"

print(f"Dear {guest[0].title()}, you are invited to the wedding aniversary of my brother.")
print(f"Dear {guest[1].title()}, you are invited to the wedding aniversary of my brother.")
print(f"Dear {guest[2].title()}, you are invited to the wedding aniversary of my brother.")
print(f"Dear {guest[3].title()}, you are invited to the wedding aniversary of my brother.")
"""
# Question 2
"""
student = "Rahul"
marks = 80
print(f"{student} scored {marks} marks.")
"""
# Question 3
"""
The below two statement is the output of the code. Now how we can create the code to get the below output. 
The first number is 10.
The sum of first two number is 30.
"""
numbers = [10, 20, 30]
print(f"The first number is {numbers[0]}.")
print(f"The sum of first two number is {numbers[0] + numbers[1]}.")
