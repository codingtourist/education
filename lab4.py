#
# lab4.py:  Bank CUstomer
#
# Bryan Hooper
# CSUFx IntroPy Fall 2016
#

# Modules
from BankCustomer import BankCustomer

# Instantiate bank customer
bank = BankCustomer('Bryan Hooper', 3000000.0)

# Print customer information
print('Welcome to Python Bank, ' + bank.name)
print('Your current balance is: ' + bank.to_dollars(bank.balance))

# Withdraw $100
bank.withdraw(100.00)

# Deposit $10,000
bank.deposit(10000.00)

# Withdraw $10,000,000.00
bank.withdraw(10000000.00)