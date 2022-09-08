f = open('readFileDefault.py', mode='r')

lines = []
for line in f:
	lines.append(line.strip())

print(lines)	
f.seek(0)


# one liner
lines = [line.strip() for line in f]
print(lines)

f.close()