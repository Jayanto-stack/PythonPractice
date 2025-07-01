# Functions: def, parameters, return values
# Python Crash Course PDF, Try it yourself solution

"""1. Question: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. 
Call the function."""
def display_message():
	"""prints one sentence telling everyone what you are learning about in this chapter. 
		Call the function, and make sure the message displays correctly."""
	print("Python Crash course book is really good book.")

display_message()

"""2. Write a function called favorite_book() that accepts one parameter, title. 
		The function should print a message, such as One of my favorite books is Alice in Wonderland.
		Call the function, making sure to include a book title as an argument in the function call."""
def favorite_book(message):
	print("One of my favorite books is " + message.title())

favorite_book("Alice in Wonderland")

# Positonal Argument
def describe_pet(animal_type, pet_name):
	""" Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title()  + ".")

describe_pet('hamster', 'harry')
describe_pet(animal_type='labrador', pet_name='Hunter')


