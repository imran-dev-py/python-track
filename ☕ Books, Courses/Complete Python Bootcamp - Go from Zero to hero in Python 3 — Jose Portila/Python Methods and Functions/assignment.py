# Functions and Methods Homework

"""
Write a function that computes the volume of a sphere given its radius.

Fromula -> (4/3)*PI*radius^3
"""


import string


def volume(radius):
    return (4 / 3) * 3.14 * pow(radius, 3)


print(volume(2))


"""
Write a function that checks whether a number is in a given
range (inclusive of high and low)

ran_bool(3,1,10) --> True
"""


def ran_check(number, low, high):
    if number >= low <= high:
        return f'{number} is in range {low} to {high}'
    return f'{number} not in range'


"""
def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')
"""

print(ran_check(5, 2, 10))
print(ran_check(3, 1, 10))


"""
Write a Python function that accepts a string and calculates
the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output :
No. of Upper case characters : 4
No. of Lower case Characters : 33
"""


def up_low(str1):
    upper = 0
    lower = 0

    for s in str1:
        if s.isupper():
            upper += 1
        elif s.islower():
            lower += 1

    print(f'Number of lowercase is -> {lower}')
    print(f'Number of uppercase is -> {upper}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


"""
Write a Python function that takes a list and returns
a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""


def unique_list(lst):
    return list(set(lst))


lst = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
print(unique_list(lst))  # [1, 2, 3, 4, 5]


"""
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
"""


def multiply(numbers):
    res = 1
    for num in numbers:
        res *= num
    return res


nums = [1, 2, 3, -4]
print(multiply(nums))  # -24

"""
Write a Python function that checks whether a passed in string is palindrome or not.

palindrome('helleh') --> True
"""


def palindrome(str1):
    new_str = str1.replace(' ', '')
    return new_str == str1[::-1]


str1 = 'madam'
print(palindrome(str1))  # True
str2 = 'helleh'
print(palindrome(str2))  # True


"""
Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing every letter of
the alphabet at least once.
For example :
"The quick brown fox jumps over the lazy dog" -- . True
"""


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print(ispangram("The quick brown fox jumps over the lazy dog"))
