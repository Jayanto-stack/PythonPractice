# A list is a collection of items in a particular order. Mutable
"""
bicycle = ['hero', 'redline', 'crossroad', 'BMX']
print(bicycle)

# Accessing Elements in a list
print(bicycle[0])       # Hero
print(bicycle[1].title())       # Redline
print(bicycle[-1])              # BMX
message = "My first bicycle was a " + bicycle[2].title() +"."
print(message)
"""
# Changing, adding and removing elements
# Modifying elements in list
"""
bicycle[0] = 'Ducati'
print(bicycle) 
"""
# Adding elements to a list --> Using Append method.
"""
bicycle.append('BMW')
print(bicycle)
"""
# Insert elements into a list
"""
bicycle.insert(1, 'Hyabusa')
print(bicycle)
"""
# Removing an item using del statement
"""
del bicycle[1]
print(bicycle)
"""
# Using pop() method remove item from the list
"""
popped_bicycle = bicycle.pop()
print(popped_bicycle)            # BMW
"""
"""
last_owned = bicycle.pop()
print("The last bicycle I owned was a "+ last_owned.title() + ".")
"""
# Organizing a list
cars = ['bmw', 'audi', 'jaguar', 'toyota', 'subaru']
cars.sort()
# print(sorted(cars))        # sorting a list temporarily using the sorted() function
print(cars)

# Printing a list in Reverse Order
cars.reverse()
print(cars)

# Finding the length of a list
print(len(cars))




