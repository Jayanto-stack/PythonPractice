# Example If loop using input function
"""
number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
"""
# While Loop
# Counting from 1 to 5
"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
"""
# Using break to exit a loop
"""
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to, " + city.title() + "!")
"""
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)