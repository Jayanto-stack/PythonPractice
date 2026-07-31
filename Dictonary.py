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

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

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

