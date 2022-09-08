import random
import string

adjectives = [
    'sleepy', 'slow', 'smelly',
    'wet', 'fat', 'red',
    'orange', 'yellow', 'green',
    'blue', 'purple', 'fluffy',
    'white', 'proud', 'brave']

nouns = [
    'apple', 'dinosaur', 'ball',
    'toaster', 'goat', 'dragon',
    'hammer', 'duck', 'panda']

colors = [
    'red', 'green', 'blue', 'yellow', 'pink',
    'ghostwhite', 'orange', 'magenta', 'white',
    'black', 'yellowgreen']

print('Welcome to password cracker')
while True:
    number = random.randrange(0, 100)
    special__charcter = random.choice(string.punctuation)
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    color = random.choice(colors)

    password = noun + adjective + special__charcter + str(number) + color
    print(f'Your password is: [{password}]')
    response = input('Would you like more passwords(y / n)? ')

    if (response == 'n'):
        break
