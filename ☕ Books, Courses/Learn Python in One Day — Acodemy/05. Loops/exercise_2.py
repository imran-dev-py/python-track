x = []

for monday in range(1, 366, 7):
    x.append(monday)

print(len(x))

# list comprehension
y = [x.append(m) for m in range(1, 366, 7)]
print(len(y))
