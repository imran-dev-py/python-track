
def check_family_guess(guess, answer):
    global score
    attempt_time = 0

    while (attempt_time < 2):
        if (guess.lower() == answer.lower()):
            print('Correct answer')
            score = score + 1
            break

        else:
            if (attempt_time < 1):
                guess = input('Sorry, Wrong answer and try again: ')
            attempt_time = attempt_time + 1

    if (attempt_time == 2):
        print(f'The Correct answer is {answer}')


score = 0
print('Guess about Mr. Alamgir\'s family')
guess_1 = input('Who is the main earning Person of this family? ')
check_family_guess(guess_1, 'Alamgir')
guess_2 = input('Who is the eldest person of this family? ')
check_family_guess(guess_2, 'Halim Mia')
guess_3 = input('How many members in this family? ')
check_family_guess(guess_3, '6')
guess_4 = input('Who is the stupid person inside the family? ')
check_family_guess(guess_4, 'Alamgir')
guess_5 = input('How many children he has? ')
check_family_guess(guess_5, '1')
guess_6 = input('What is his wife name? ')
check_family_guess(guess_6, 'Mitu')

print(f'Congrats! for finish the survey and your score is {score}')
