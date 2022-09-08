# Statement Assessment test

```py
Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
split_str = st.split()

# Normal version
for word in split_str:
  if word[0] == 's':
    print(word)

# list comprehension version
[print(word) for word in split_str if word[0] == 's']
```

```py
Use range() to print all the even numbers from 0 to 10

even = [number for number in range(0,11) if number % 2 == 0]
print(even)

# shorter
even = list(range(0,11,2))
print(even)
```

```py
Use a List Comprehension to create a list of all numbers between 1 and 50 that are evenly divisible by 3.

numbers = [num for num in range(1, 51) if num % 3 == 0]
print(numbers)
```

```py
Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
split_str = st.split()

for x in split_str:
    if len(x) % 2 == 0:
        print(x+" <-- has an even length!")

# list comprehension version
[print('even!') for x in split_str if len(x) % 2 == 0]
```

```py
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
```

```py
Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
st = st.split()

new_str = [x[0] for x in st]
print(new_str)
```
