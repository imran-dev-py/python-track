try:
    age = int(input('Age: '))
except ValueError as e:
    print(e)
else:
    print(age)


# raise exception if u really need to in ur code cause it takes so much time
