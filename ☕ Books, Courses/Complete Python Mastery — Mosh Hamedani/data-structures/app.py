# list unpacking

numbers = list(range(0, 11))
first, _, *others, last = numbers
print(first)
print(others)

# remove methods
nums = list(range(11))
nums.clear()  # it's removes all items & return empty []
del nums  # del the nums
# print(nums) [num is not defined]

# sort list of tuples
items = [
    ('product_1', 900),
    ('product_2', 800),
    ('product_3', 500)
]

items.sort(key=lambda item: item[1])
print(items)

# map(func, *iterable)
prices = list(map(lambda item: item[1], items))
print(prices)

# filter(func, *iterable)
greater_10 = list(filter(lambda itemPrice: itemPrice[1] > 500, items))
print(greater_10)

# with list comprehension
greater_10 = [(item, price) for item, price in items if price > 500]
print(greater_10)

x = [1, 2, 3]
y = [10, 20, 30]
xy = list(map(lambda x, y: (x, y), x, y))
print(xy)

print(list(zip(x, y)))
