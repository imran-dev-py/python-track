# Python Quiz


def quiz(guess, answer):
    attempt = 0
    global score

    while (attempt <= 1):
        if (guess.lower() == answer.lower()):
            print('Correct answer')
            score = score + 2
            break

        else:
            attempt = attempt + 1

    if attempt == 2:
        print(f'Try again and answer is [{answer}]')


score = 0
print('Let\'s try Python Quiz')
guess_1 = input('Who is the founder of Python? ')
quiz(guess_1, 'Guido van Rossum')
guess_1 = input('Which year he created it? ')
quiz(guess_1, '1980')
guess_3 = input('What is the python Web Framework? ')
quiz(guess_3, 'Django')
guess_4 = input('What is the best book for python? ')
quiz(guess_4, 'python Crash Course')
guess_5 = input('Whih version currently Python has? ')
quiz(guess_5, '3.x')
print(f'Congrats! for finish quiz and your score is {score}')
