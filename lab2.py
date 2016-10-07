#
# lab2.py:  Guess the Number
#
# Bryan Hooper
# CSUFx IntroPy Fall 2016
#

# Main variables
correct_num = 6
no = 0

# Define instructions
instruction = 'Guess a number from 1 to 10.  Enter 0 to exit.'
prompt = 'Guess the number: '

# Begin game
print(instruction)

while True:
	guess = input(prompt)	
	guess = int(guess)

	if guess == 0:
		print('Exiting: Game Over!')
		break
	elif guess == correct_num:
		print('YOU ARE CORRECT!  Game Over')
		break
	elif guess < 0 or guess > 10:
		print('Bad guess! [%s]' % (instruction))
		prompt = 'Guess again: '
	elif guess < correct_num:
		prompt = 'Too low! Guess again: '
	elif guess > correct_num:
		prompt = 'Too high! Guess again: '
	else:
		print('Bad guess! [%s]' % (instruction))
		prompt = 'Guess again: '
		continue


