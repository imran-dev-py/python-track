# create a new list of tuples, each consisting of a Boolean value and the 
# original string. The Boolean value indicates whether the string 'anonymous' 
# appears in the original string! 

txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

mark = list(map(lambda line : (True, line) if 'anonymous' in line else (False, line), txt))

print(mark)