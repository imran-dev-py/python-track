"""
Rules for variable names
* Names can't start with number.
* There can be no spaces in the variable name use insted _
* Can't use any symbol
* Avoid python special keyword
"""
x_py = 78
print(x_py)

a = 5
print(a)
a = 10
print(a)

a += a
print(a)
print(type(a))

a = 3.0
print(id(a))
print(type(a))

my_income = 100
tax = .1
my_taxes = my_income * tax
print(my_taxes)
