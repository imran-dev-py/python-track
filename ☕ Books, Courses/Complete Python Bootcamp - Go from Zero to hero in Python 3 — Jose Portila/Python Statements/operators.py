
# enumerate() [takes any iterable obj and return tuple of index with obj]
for count, letter in enumerate('abcde'):
    print(f'At index {count} letter is {letter}')

print()
# without enumerate
count = 0

for letter in 'abcde':
    print(f'At index {count} letter is {letter}')
    count += 1


# zip() [combines 2 iterable obj return tuple of (1st[0], 2nd[0])]
# zip returns a generator

x = range(0, 5)
y = range(6, 11)

for item in zip(x, y):
    print(item)


# List comprehension
# if i want to use if else then i need to follow this way
even_odd = [x if x % 2 == 0 else 'odd' for x in range(2, 20)]
print(even_odd)

# normal list comprehension
odd = [y for y in range(0, 20) if y % 2 != 0]
print(odd)

# nested list comprehension
mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)

# Nested loop
new = []

for x in range(11):
    for y in [x ** 2]:
        new.append(y**2)

print(new)

# list comprehension version
lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst)
