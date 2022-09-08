"""
* If word start with a vowel, add 'ay' to end
* If word does not start with a vowel, put first letter at the end,
then add 'ay'
* word --> ordway
* apple -> appleay
"""


def pig_latin(word):
    if word[0] in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'


print(pig_latin('word'))
print(pig_latin('apple'))


# find out if the 'dog' is in string

def dog_check(string):
    return 'dog' in string.lower()


print(dog_check('dog ran away'))
