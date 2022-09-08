"""
MAP ->
The map function allows you to "map" a function to an iterable object. That is
to say you can quickly call the same function to every item in an iterable, such as a list
"""


def square(num):
    return num * 2


num = list(range(1, 6))
squares = list(map(square, num))
print(squares)


def square2(num):
    new = [num_ * 2 for num_ in num]
    return new


nums = list(range(1, 6))
print(square2(nums))


"""
FILTER -> [Deep study need]
The filter function returns an iterator yielding those items of iterable
for which function(item) is true. Meaning you need to filter by a
function that returns either True or False. Then passing that into
filter (along with your iterable) and you will get back only the
results that would return True when passed to the function.
"""


def check_even(nums):
    return nums % 2 == 0


nums = list(range(0, 11))
even_numbers = list(filter(check_even, nums))
print(even_numbers)

# Except filter function


def check_even2(nums):
    even_numbers = []
    for num in nums:
        if num % 2 == 0:
            even_numbers += [num]
    return even_numbers


print(check_even2(nums))

# Lambda Expression


def square(num):
    return num ** 2


print(square(20))

"""
lambda ->
    square = lambda num: num ** 2
    print(square(2))
"""
