# args
def myfunc(*a):
    print(a)  # return tuples
    return sum(a) * .05


print(myfunc(10, 20, 30))


# kwargs
def myFunc(**kwargs):
    print(kwargs)  # return dict

    if 'fruit' in kwargs:
        name = kwargs['fruit']
        print(f'My fruit of choice is {name}')
    else:
        print('I did not find any fruit here')


myFunc(fruit='apple', vegetable='ladies finger')


# combine

def basic_info(*names, **occupations):
    print(names)
    print(occupations)
    name = f'My name is {names[1]}'
    occupation = 'and occupation is {0} at Yandex'.format(
        occupations['yandex'])
    print(name, occupation)


basic_info('Kamal', 'Imran', 'Jhony', 'Bonny', yandex='Software engineer')
