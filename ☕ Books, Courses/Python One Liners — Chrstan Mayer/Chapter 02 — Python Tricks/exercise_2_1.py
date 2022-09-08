# create a new list of tuples, each consisting of a Boolean value and the 
# original string. The Boolean value indicates whether the string 'anonymous' 
# appears in the original string! 

# Use list comprehension rather than the map() function to accomplish the same output.

txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

mark = [(True, line) if 'anonymous' in line else (False, line) for line in txt]
print(mark)