# Our goal is to replace every other string with the string immediately in front of it;

visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

# one liner
visitors[1::2] = visitors[::2] # corrupted = Firefox
print(visitors)

# my for loop solution
for index, browser in enumerate(visitors):
    if browser == 'corrupted': visitors[index] = visitors[i-1]

print(visitors)

"""
visitors = ['Firefox', 'Firefox', 'Chrome', 'Chrome',
            'Safari', 'Safari', 'Safari', 'Safari',
            'Chrome', 'Chrome', 'Firefox', 'Firefox']
"""