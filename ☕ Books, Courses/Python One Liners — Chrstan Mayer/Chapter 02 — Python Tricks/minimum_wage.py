"""
Our data is a dictionary of dictionaries storing the hourly wages of company employees. You want to extract a list of the companies paying below your state’s minimum wage (< $9) for at least one employee;
"""


companies = {
	'CoolCompany': {
		'Alice': 33, 
		'Bob': 28,
		'Frank': 29
	},
	'CheapCompany': {
		'Ann': 4,
		'Lee': 9,
		'Christ': 7
	},
	'SosoCompany': {
		'Esther': 38,
		'Cole': 8,
		'Paris': 18
	}
}

illegal = [x for x in companies if any(y<9 for y in companies[x].values())]
print(illegal)