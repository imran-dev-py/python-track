# keyword args


def increment(number, by):
    return number + by


print(increment(number=10, by=4))

# positional args


def increment2(number, by):
    return number + by


print(increment2(20, 5))

# default parameters


def increment3(number, by=8):
    return number + by


print(increment3(20))
