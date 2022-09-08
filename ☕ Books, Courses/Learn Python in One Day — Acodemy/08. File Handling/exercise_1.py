files = ['1145', '1132', '1139', 'No data', '1141']

with open('abc.txt', 'w') as file:
    for file_ in files:
        file.write(file_ + '\n')

with open('abc.txt', 'r') as file:
    content = file.read()
    print(content)
