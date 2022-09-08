'''
For object-oriented programming in Python, this means that a particular object
belonging to a particular class can be used in the same way as if it were a
different object belonging to a different class.

When several classes or subclasses have the same method names, but different
implementations for these same methods, the classes are polymorphic because
they are using a single interface to use with entities of different types.
A function will be able to evaluate these polymorphic methods without
knowing which classes are invoked.
'''
'''
Polymorphism (in the context of object-oriented programming) means a subclass can
override a method of the base class. This means a method of a class can do
different things in subclasses. For example: a class Animal can have a method
talk() and the subclasses Dog and Cat of Animal can let the method talk() make different sounds.

Duck typing means code will simply accept any object that has a particular method.
Let's say we have the following code: animal.quack(). If the given object animal
has the method we want to call then we're good (no additional type requirements needed).
It does not matter whether animal is actually a Duck or a different animal
which also happens to quack. That's why it is called duck typing: if
it looks like a duck (e.g., it has a method called quack()
then we can act as if that object is a duck).
'''


class Shark():
    def swim(self):
        print('The Shark is swimming')

    def backwards_swim(self):
        print('The shark cannot swim backwards, but can sink backwards.')

    def skeleton(self):
        print('The shark\'s skeleton is made of cartilage.')


class ClownFish():
    def swim(self):
        print('The clownfish is swimming.')

    def backwards_swim(self):
        print('The clownfish can swim backwards.')

    def skeleton(self):
        print('The clownfish\'s skeleton is made of bone.')


sammy = Shark()
sammy.swim()

casey = ClownFish()
casey.skeleton()

print()
# Polymorphism with Class Methods
for fish in (sammy, casey):
    fish.swim()
    fish.skeleton()
    fish.backwards_swim()

# Polymorphism with a Function
