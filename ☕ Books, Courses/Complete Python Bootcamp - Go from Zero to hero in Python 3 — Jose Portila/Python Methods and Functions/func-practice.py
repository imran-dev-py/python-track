"""
Write a function that returns the lesser of two given numbers if both
numbers are even, but returns the greater if one or both numbers are odd

lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""


def lesser_of_two_evens(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min([num1, num2])
    else:
        return max([num1, num2])


print(lesser_of_two_evens(4, 2))
print(lesser_of_two_evens(2, 5))

"""
Write a function takes a two-word string and returns True if both words
begin with same letter

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""


def animal_crackers(str1):
    str1 = str1.split()
    return str1[0][0] == str1[1][0]


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

"""
Given two integers, return True if the sum of the integers is 20 or if
one of the integers is 20. If not, return False

makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""


def makes_twenty(a, b):
    return sum([a, b]) == 20 or (20 in [a, b])


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))


# LEVEL 1 PROBLEMS

"""
Write a function that capitalizes the first and fourth letters of a name

old_macdonald('macdonald') --> MacDonald
"""


def old_macdonald(str1):
    new_macdonald = str1[0].upper() + str1[1:3] + str1[3].upper() + str1[4:]
    return new_macdonald


print(old_macdonald('macdonald'))


"""
MASTER YODA: Given a sentence, return a sentence with the words reversed

master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
"""


def master_yoda(sentence):
    sentence = sentence.split()
    sentence.reverse()
    return ' '.join(sentence)


print(master_yoda('I am home'))
print(master_yoda('We are ready'))

"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
"""


def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# LEVEL 2 PROBLEMS

"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""


def has_33(numbers):
    for num in range(0, len(numbers) - 1):
        if (numbers[num] == 3) and (numbers[num + 1] == 3):
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

"""
PAPER DOLL: Given a string, return a string where for every character in the
original there are three characters

paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""


def paper_doll(str1):
    return ''.join([w * 3 for w in str1])


print(paper_doll('Hello'))
print(paper_doll('Mississippni'))

"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than
or equal to 21, return their sum. If their sum exceeds 21 and there's an
eleven, reduce the total sum by 10. Finally,
if the sum (even after adjustment) exceeds 21, return 'BUST'

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
"""


def blackjack(a, b, c):
    sumOf = sum([a, b, c])
    if sumOf <= 21:
        return sumOf
    else:
        if (11 in [a, b, c]):
            sumOf -= 10
            return sumOf
        else:
            return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore
sections of numbers starting with a 6 and extending to the next 9
(every 6 will be followed by at least one 9). Return 0 for no numbers

summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
"""


def summer_69(nums):
    total = 0
    is_boolean = True

    for num in nums:
        if num >= 10:
            is_boolean = True
        while is_boolean:
            if num != 6:
                total += num
                break
            is_boolean = False

        while True:
            if num != 9:
                break
            break
    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# CHALLENGING PROBLEMS

"""
SPY GAME: Write a function that takes in a list of integers and returns
True if it contains 007 in order

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""


def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

"""
COUNT PRIMES: Write a function that returns the number of prime numbers
that exist up to and including a given number

count_primes(100) --> 25
"""


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


print(count_primes(100))

"""
PRINT BIG: Write a function that takes in a single letter, and returns
a 5x5 representation of that letter

print_big('a')
out:   *
      * *
     *****
     *   *
     *   *
"""


def print_big(letter):
    patterns = {
        1: '  *  ',
        2: ' * * ',
        3: '*   *',
        4: '*****',
        5: '**** ',
        6: '   * ',
        7: ' *   ',
        8: '*   * ',
        9: '*    '

    }

    alphabets = {
        'A': [1, 2, 4, 3, 3],
        'B': [5, 3, 5, 3, 5],
        'C': [4, 9, 9, 9, 4],
        'D': [5, 3, 3, 3, 5],
        'E': [4, 9, 4, 9, 4]
    }

    for pattern in alphabets[letter.upper()]:
        print(patterns[pattern])


print_big('d')
