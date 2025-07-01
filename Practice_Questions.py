# Practice Questions
'''
Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance
'''

class Account:
	def __init__(self, bal, acc):
		self.balance = bal
		self.account_no = acc

	#debit account
	def debit(self, amount):
		self.balance -= amount
		print("Rs.", amount, "was debited")
		print("total balance =", self.get_balance())

	#Credited account
	def credit(self, amount):
		self.balance += amount
		print("Rs.", amount, "was credited")
		print("total balance =", self.get_balance())

	#Return final balance
	def get_balance(self):
		return self.balance

acc1 = Account(10000, 23424)
acc1.debit(1000)
acc1.credit(500)

