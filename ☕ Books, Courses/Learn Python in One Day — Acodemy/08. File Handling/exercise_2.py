
new_content = []
with open('abc.txt', 'r') as file:
    content = file.readlines()

    for item in content:
        new_content.append(item.strip('\n'))
    print(new_content)
