# Checking Whether a Value is not in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(user.title()+", you can post a response if you wish.")

else:
	print("The user name is already in list")


# If-else example code

age = 16
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

# if-elif-else Chain
"""
Task:
- Admission for anyone under age 4 is free.
- Admission for anyone between the ages of 4 and 18 is $5.
- Admission for anyone age 18 or older is $10.
"""
age = 22
if age < 5:
	print("Your admission cost is $0.")

elif age < 19:
	print("Your admission cost is $5.")

else:
	print("your admission cost is $10.")

# Try it Yourself:
# Alien Colors
"""
Imagine an alien was just shot down in a game. Create a variable called alien_color and assign if a value of 'green', 'yellow', or 'red'.
- Write an if statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.
- Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

"""

alien_color = 'green'
if alien_color == 'green':
	print("You have earned 5 points!")

else:
	print("You answer is incorrect, better luck next time!")





