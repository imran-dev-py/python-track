mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_number = [num for num in mylist if num % 2 == 0]
print(even_number)
odd_number = [num for num in mylist if num % 2 != 0]
print(odd_number)

for _ in 'hello':
    print('cool!')

# list unpacking
my_tup = [(1, 2), (3, 4), (5, 6), (7, 8)]
a, b, c, d = my_tup
print(a, b, c, d)
print([a for (a, b) in my_tup])

# tuple unpacking
my_tuple = (4, 5, 6, 8)
a, _, b, _ = my_tuple
print(a, b)

# dict
my_dict = {
    'k1': 'One',
    'k2': 'Two',
    'k3': 'Three'
}
print({key: value for key, value in my_dict.items()})

x = list(range(11))

for xx in x:
    if xx == 5:
        break
    print(xx)
else:
    print('Done!')

# done not printed because using break keyword
# it breaks out the loop, same as while
