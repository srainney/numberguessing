import random

print('------------------------')
print('    GUESS THE NUMBER')
print('------------------------')
print('')

name = input('What is your name? ')
# Generates a random number between 0 and 100
the_number = random.randint(1, 99)
# Used to initiate the while statement
guess = "text"

while guess != the_number:
    # Checking if the supplied value is within the specified range
    try:
        guess = int(input('Guess a whole number between 0 and 100: '))
    except ValueError:
        print('That is not a whole number between 0 and 100. Please try again.')
        continue
    if 0 < guess < 100:
        pass
    else:
        print('That is not a whole number between 0 and 100. Please try again.')
        continue
    # Prints the output for each guess
    if guess < the_number:
        print('Sorry, {}, your guess of {} was too low.'.format(name, guess))
    elif guess > the_number:
        print('Sorry, {}, your guess of {} was too high.'.format(name, guess))
    else:
        print('You win, {}! Congratulations!'.format(name))

input('Press ENTER to exit')