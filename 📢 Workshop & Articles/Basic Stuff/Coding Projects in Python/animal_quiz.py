def check_guess(guess, answer):
    attempt = 0
    still_guessing = True
    global score

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            #score = score + 1
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Wrong answer ')
            attempt = attempt + 1

    if attempt == 3:
        print('The Correct answer is ' + answer)


score = 0
print('Guess the animal!!')
guess_1 = input('Which bear lives at the North Pole? ')
check_guess(guess_1, 'Polar Bear')
guess_2 = input('Which is the largest animal? ')
check_guess(guess_2, 'Blue whael')
guess_3 = input('Which is the fastest land animal? ')
check_guess(guess_3, 'Cheetah')
print(f'Your Score is {score}')
