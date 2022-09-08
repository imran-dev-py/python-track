employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121
         }

top_earners = []

for name, salary in employees.items():
	if salary >= 100_000:
		top_earners.append((name, salary))

print(top_earners)

# one liners
print([(name, salary) for name, salary in employees.items() if salary >= 100_000])