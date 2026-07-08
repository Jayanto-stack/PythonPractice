# A list is a collection of items in a particular order.

bicycle = ['Hero', 'redline', 'Cross', 'BMX']
print(bicycle)

# Accessing Elements in a list
print(bicycle[0])
print(bicycle[1].title())
print(bicycle[-1])
message = "My first bicycle was a " + bicycle[2].title() +"."
print(message)

# Changing, adding and removing elements
# Modifying elements in list
bicycle[0] = 'Ducati'
print(bicycle)

# Adding elements to a list --> Using Append method.
# bicycle.append('BMW')
# print(bicycle)

# Insert elements into a list
bicycle.insert(1, 'Hyabusa')
print(bicycle)

# Removing an item using del statement
"""
del bicycle[1]
print(bicycle)
"""
# Using pop() method remove item from the list
"""
popped_bicycle = bicycle.pop()
print(popped_bicycle)
"""
last_owned = bicycle.pop()
print("The last bicycle I owned was a "+ last_owned.title() + ".")




