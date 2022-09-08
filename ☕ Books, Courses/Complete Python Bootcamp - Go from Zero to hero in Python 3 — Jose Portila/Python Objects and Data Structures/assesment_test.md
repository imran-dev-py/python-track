# Objects and Data Structures Assessment Test

```py
Write a brief description of all following Object types and data structure we've learned about

strings -> collection of Order sequence characters
Numbers -> Store numerical information
lists -> collection of order sequence objects (mutable)
Tuples -> collection of order sequences objects (immutable)
dictionaries -> collection of key:value pairs
```

## Numbers

```py
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
(60 + (10 ** 2) / 4 * 7) - 134.75

Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 * (6 + 5)
Answer -> 44
What is the value of the expression 4 * 6 + 5
Answer -> 29
What is the value of the expression 4 + 6 * 5
Answer -> 34

What is the type of the result of the expression 3 + 1.5 + 4?
Answer -> <class 'float'>

What would you use to find a number’s square root, as well as its square?
# Square root -> exponent (**) 4 ** .5
# Square -> exponent (**) 2.0 ** 2
```

## Strings

```py
Given the string 'hello' give an index command that returns 'e'.
s = 'hello'
print(s[1])
print(s[-4])

Reverse the string 'hello' using slicing:
s = 'hello'
print(s[::-1])

Given the string hello, give two methods of producing the letter 'o' using indexing.
s = 'hello'
print(s[len(hello) -1])
print(s[-1])
```

## Lists

```py
Build this list [0,0,0] two separate ways.
# Method 1 ->
listOfZeros = [0]*3
print(listOfZeros)

# Method 2 ->
listOfZeros = []
listOfZeros.extend([0,0,0])
print(listOfZeros)

Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

Sort the list below:
list4 = [5,3,4,6,1]
sorted_list = sorted(list4)
print(sorted_list)
```

## Dictionaries

```py
Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {
'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]
}
print(d['k1'][2]['k2'][1]['tough'][2][0])

Can you sort a dictionary? Why or why not?
# Answer ->
No! Because normal dictionaries are mappings not a sequence
```

## Tuples

```py
What is the major difference between tuples and lists?
# Answer ->
Major difference between tuples and lists are list is mutable and tuples is not.

How do you create a tuple?
x = (1, 2)
```

## Sets

```py
What is unique about a set?
They don't allow for duplicate items.

Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

```

## Boolean

```py
What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

2 > 3
# Answer -> False
3 <= 2
# Answer -> False
3 == 2.0
# Answer -> False
3.0 == 3
# Answer -> True
4**0.5 != 2
# Answer -> False

Final Question: What is the boolean output of the cell block below?

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
# Answer -> False
```
