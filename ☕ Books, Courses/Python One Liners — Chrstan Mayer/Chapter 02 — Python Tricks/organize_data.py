column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
	('Bob', 99000, 'mid-level manager'),
	('Frank', 87000, 'CEO')]


db = [dict(zip(column_names, rows)) for rows in db_rows]
print(db)

"""
[{'name': 'Alice', 'salary': 180000, 'job': 'data scientist'},{'name': 'Bob', 'salary': 99000, 'job': 'mid-level manager'},{'name': 'Frank', 'salary': 87000, 'job': 'CEO'}]
"""