with open('abc.txt', 'w') as file:
    file.write('Hello, Word')
with open('abc.txt') as file:
    print(file.read())
    file.seek(0)
    print(file.read())

# read return everything in string format and readlines return list of str
with open('my_text.txt', mode='w') as file:
    file.writelines('One is One\nTwo is Two\nThree is three')

with open('my_text.txt', 'r') as file:
    print(file.read())
