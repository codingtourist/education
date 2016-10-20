#
# BankCustomer.py:  Class to support lab4.py
#
# Bryan Hooper
# CSUFx IntroPy Fall 2016
#

class BankCustomer(object):

	""" Class for bank customer data and actions """

	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def to_dollars(self, amount):
		amount = round(amount, 2)
		dollar_amount = '$' + format(amount, '6,.2f')
		return dollar_amount

	def deposit(self, amount):
		print('Depositing ' + self.to_dollars(amount) + '...')
		self.balance = self.balance + amount
		print('Your new balance is ' + self.to_dollars(self.balance))

	def withdraw(self, amount):
		print('Withdrawing ' + self.to_dollars(amount) + '...')
		if amount > self.balance:
			print('Transaction cancelled!  Your account balance is only ' + self.to_dollars(self.balance))
		else:
			self.balance = self.balance - amount
			print('Your new balance is ' + self.to_dollars(self.balance))