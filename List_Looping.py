# Looping through an entire list
# For Loop
# We use the for loop, where we have to do the same task again and again.
"""
magicians = ['alice','gogiya sarkar', 'sachin', 'dhoni', 'op sharma']
for jadugar in magicians:
    print(jadugar.title() + ", he is a great person.")
    print("Can't wait to see"+ " " + jadugar.title() +"'s " + " "+ "performance."+ "\n")
"""
# range() function
"""
for value in range(0,7):
    print(value)
"""
# using range() to make a list of numbers
"""
numbers = list(range(0,10))
print(numbers)
"""
"""
odd_numbers = list(range(1, 30, 5))
print(odd_numbers)
"""
# Simple Statistics with a list of numbers
"""
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
"""
# Slicing of a list
# players = ['ronaldo', 'messi', 'maradona', 'pele', 'kohli']
# print(players[0:2])
# print(players[1:5])

# Create a list, and implement for loop, output should print using slicing method.
"""
print("Here are the list of first three players on my team:")
for player in players[:3]:
    print(player.title())
"""
# Copying a list
my_foods = ['pizza', 'burger', 'chole kulche', 'chole bhature']
friends_foods = my_foods[0:2]

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friends_foods)
