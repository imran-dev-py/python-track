class Dog():

    # Class object attribute
    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name

        # Except boolean True/False
        self.spots = spots

    def res(self):
        print(self.breed)
        print(self.name)
        print(self.spots)


my_dog = Dog('lab', 'sammy', True)
print(type(my_dog))
my_dog.res()
print(my_dog.species)
