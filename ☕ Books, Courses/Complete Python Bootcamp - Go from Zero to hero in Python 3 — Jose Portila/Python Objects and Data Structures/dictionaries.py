# Collection of key:value pairs

my_dict = {
    'Key1': 'Value',
    'Key2': 'Value2'
}

print(my_dict)

d = {
    'k1': 456,
    'k2': [4, 5, 6],
    'k3': {'k3_1': 789}
}
print(d['k3']['k3_1'])

dd = {}
dd['0'] = 1
print(dd)

dd = tuple()
print(dd)

try:
    ddd = dict(['0', 1], [('1', 2)])
except:
    print('Error')
else:
    print(ddd)
