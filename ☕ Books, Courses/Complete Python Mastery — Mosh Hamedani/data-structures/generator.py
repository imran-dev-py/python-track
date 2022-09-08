import sys

values = (x*2 for x in range(1000))
print(values)
print(sys.getsizeof(values))

# unpacking operator [need deep study]
print(list('hello'))
print([*'hello'])

# unpacking dict
first  = dict(x = 2)
second = dict(a = 10, y = 20)
combined = dict(**first, **second, z = 5)
print(combined)