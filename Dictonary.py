# Dictionary
"""
A dictionary is a collection of key-value pairs. Each key is connected to a value, 
and you can use a key to access the value associated with that key.
A dictionary is wrapped in braces {}.
"""
# Consider a game featuring aliens that can have different colors and point values.
"""
alien_0 = {'color': 'green', 'points': 5}
# Accessing values in a dictionary
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding New key-Value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
"""
# Starting with an Empty Dictionary
"""
alien_0 = {}

alien_0['color'] = 'brown'
alien_0['points'] = 7
print(alien_0)

# Modify values in Dictionary
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
print(alien_0)

# Removing key-value Pairs
del alien_0['points']
print(alien_0)
"""
# Create a dictionary of different students language learned
"""
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
"""
# Looping, for loop
"""
user_0 = {
    'username': 'jayanto98',
    'first': 'jayanto',
    'last': 'mukhopadhyay'
}
for key, value in user_0.items():
    print("\nkey: " + key)
    print("Value: " + value)
"""
# A list of Dictionaries
"""
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'black', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
"""
# Make an empty list for storing items
"""
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    print(alien)

# Show the next 15 aliens
for alien in aliens[5:15]:
    print(alien)

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
"""

# Store information about a pizza being ordered
"""
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order
print("You have ordered a " + pizza['crust'] + "-crust pizza" + " with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
"""

# Nest list inside a dictionary
"""
favorite_languages = {
    'mark': ['python', 'ruby'],
    'edward': ['c'],
    'modiji': ['hindi', 'python'],
    'cjp': ['r', 'go']
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
"""
# Looping using key-value pairs
"""
user_0 = {
    'username': 'JSMSec',
    'first': 'Jayanto',
    'last': 'Mukhopadhyay'
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
"""
#
"""
favourite_languages = {
    'jayanto': 'python',
    'chandan': 'java',
    'rohan': 'c',
    'shruti': 'ruby'
}
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
print("The follwoing languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())
"""
"""
Make a dictionary containing three major cities and their rivers:
    - Use a loop to print a sentence about each river, such as 'The Ganga river is
        purest river in banaras'.
    - Use a loop to print the name of each river included in dictionary.
    - Use a loop to print the name of each cities included in dictionary.
"""
rivers_cities = {
    'banaras': 'ganga',
    'gujrat': 'narmada',
    'delhi': 'yamuna',
    'korba': 'hasdeo'
}
for citie, river in rivers_cities.items():
    print("The " + river.title() + " river is purest river in " + citie.title() + ".")

for river in rivers_cities.values():
    print(river.title())

for citie in rivers_cities.keys():
    print("\n" + citie.title())
