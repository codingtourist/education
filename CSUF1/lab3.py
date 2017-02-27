#
# lab3.py:  
#
# Bryan Hooper
# CSUFx IntroPy Fall 2016
#

# Library imports
import re

# Functions
def count_coins(bill, coin_value):
	updated_bill = bill % coin_value
	coin_count = bill // coin_value

	return updated_bill, coin_count


# Main dicts
change = {'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}
coin_values = {'quarter' : 25, 'dime': 10, 'nickel': 5, 'penny': 1}

# Request user input
instructions = 'Enter the amount of the bill (use two decimals only): '
while True:
	bill = input(instructions)

	# Validate data
	if re.search(r'^[0-9]+\.[0-9][0-9]$', bill):
		bill = bill.replace('.', '')
		break
	else:
		instructions = 'Only provide bill in a two decimal format such as 2.52: '


# Begin converting bill to change
remaining_bill = int(bill)

while remaining_bill > 0:

	if remaining_bill >= coin_values['quarter']:
		remaining_bill, change['quarter'] = count_coins(remaining_bill, coin_values['quarter'])
	elif remaining_bill >= coin_values['dime']:
		remaining_bill, change['dime'] = count_coins(remaining_bill, coin_values['dime'])
	elif remaining_bill >= coin_values['nickel']:
		remaining_bill, change['nickel'] = count_coins(remaining_bill, coin_values['nickel'])
	elif remaining_bill >= coin_values['penny']:
		remaining_bill, change['penny'] = count_coins(remaining_bill, coin_values['penny'])
	else:
		break	

# Report change required
print('Paying the bill in change requires:')
print(change['quarter'], 'quarter(s)', change['dime'], 'dime(s)', +
	  change['nickel'], 'nickel(s)', change['penny'], 'penny/pennies')
