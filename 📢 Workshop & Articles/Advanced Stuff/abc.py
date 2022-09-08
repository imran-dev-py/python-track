# Generator is much better than normal function
# iterable = > any value that can produce stream of values
# iterator = > is the object that knows where you are in that stream

def evens_generator(stream):
    for n in stream:
        if n % 2 == 0:
            yield n


def evens_(stream):
    res = []

    for n in stream:
        if n % 2 == 0:
            res.append(n)
    return res


nums = range(11)
for n in evens_(nums):
    print(n)

for n in evens_generator(nums):
    print(n)


