# A list is a collection of items in a particular order.
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
# f-string ---> You can put expressions inside {}
guest = ['Ram', 'Shayam', 'raju', 'jagdish']
print(f"\nSorry, {guest[3].title()} can't make it.")
guest[3] = "Elon Musk"

print(f"Dear {guest[1].title()}, you are invited to dinner.")   # f-string formatted string literal
print(f"Dear {guest[0].title()}, you are invited to dinner.")
print(f"Dear {guest[2].title()}, you are invited to dinner.")
print(f"Dear {guest[3].title()}, you are invited to dinner.")


