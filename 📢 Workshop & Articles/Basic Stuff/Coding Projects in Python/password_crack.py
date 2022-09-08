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

colors = ['red', 'blue', 'yellow', 'green', 'orange', 'black',
          'white', 'yellowgreen', 'ghostwhite']
print('Lets generate a random password')

while True:
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    number = random.randrange(0, 99)
    special_character = random.choice(string.punctuation)
    color = random.choice(colors)

    password = noun + adjective + \
        str(number) + special_character + color + \
        special_character + noun + adjective

    response = int(input('Enter number how many char you want: '))

    if ((response < len(password)) and ((response >= 8) and (response <= 25))):
        print(password[0:response])
    else:
        print('Password must be 8+ and less than 25')

    res = input('Would you like to generate new one [y\n]: ')
    if (res == 'n'):
        break
