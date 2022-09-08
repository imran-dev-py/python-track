# check and compare string
compare_str = 'bag' == 'Bag'
print(compare_str)
# ord() return unicode point for a single str
print(ord('b'))  # 98
print(ord('B'))  # 66

# ternary operator
age = 22
print('Eligible' if age >= 18 else 'Not eligible')

# chaining comparison operator
# age should be between 18 and 65

age = 22
if 22 >= 18 <= 65:
    print('Congrats! You\'re an adult')
else:
    print('Try next year')
