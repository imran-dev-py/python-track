"""
When you create a variable name in Python the name is stored in a name-space.

In simple terms, the idea of scope can be described by 3 general rules:
* Name assignments will create or change local names by default.
* Name references search (at most) four scopes, these are:
    local
    enclosing functions
    global
    built-in
* Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.
"""

x = 25


def xx():
    x = 50
    return x


print(x)  # 25
print(xx())  # 50
print(x)  # 25

# local
"""
f = lambda x : x + 2
print(f(2)) """


""" enclosing functions """


def info(name):
    name = "Micheal"  # name is changed
    print(name)


info('Jordan')

""" Global """

name = "Madina"


def basic_info():
    print(name)


basic_info()

# Built in name -> len, str

# local variable
x = 50


def func(x):
    print('x is', x)  # 50
    x = 2
    print('Changed local x to', x)  # 2


func(x)
print('x is still', x)  # 50


# with global keyword
x = 50


def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)  # 50
    x = 2
    print('Ran func(), changed global x to', x)  # 2


print('Before calling func(), x is: ', x)  # 50
func()
print('Value of x (outside of func()) is: ', x)  # 2
