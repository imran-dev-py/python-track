# String is a sequence of character

greeting = 'Hello, World'
print(greeting[0:5])

print(len('52'))

my_str = "Hola, Que tal"
print(my_str[::-1])  # reverse the str

my_str = 'abcdefghijkl'
print(my_str[:3:2])
print(my_str[::-5])


# Immutable [can't change]
name = 'Sam'
name = list(name)
name[0] = 'P'
print(str(''.join(name)))

name = 'Sam'
last_letters = name[1:]
print(last_letters)
print('P' + last_letters)

str_ = 'Hi, this is a string'
print(str_.split())

x = 'This is a {0}'.format('string')
print(x)

fox_quote = "The {2} brown {1} jump {0} the city".format(
    'over', 'fox', 'quick')
print(fox_quote)
