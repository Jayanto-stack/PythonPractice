'''
class Student:
	def __init__(self, fullname):
		self.name = fullname
		print("adding new student in Database..")

s1 = Student("karan")
print(s1.name)

s2 = Student("Arjun")
print(s2.name)
'''
'''
# Implementing Methods
class Student:
	college_name = "Avish Educom"
	def __init__(self, name, marks):
		self.name = name
		self.marks = marks

	def welcome(self):
		print("welcome students")

	def get_marks(self):	# implementing methods
		return self.marks

s1 = Student("karan", 75)
s1.welcome()
print(s1.name, s1.marks)
print(s1.get_marks())
'''
# Practice Question:
# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average

class Student:
	def __init__(self, name, marks):
		self.name = name
		self.marks = marks

	@staticmethod
	def hello():
		print("hello")

	def get_avg(self):
		sum = 0
		for val in self.marks:
			sum += val
		print("hi", self.marks, "is your marks and, your avg score is:", sum/3)

s1 = Student("karan", [75, 80, 78])
print(s1.name)
s1.get_avg()
s1.hello()




