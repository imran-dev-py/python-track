'''
Class — Class is a blueprint created by the programmer for an object.
Object — An instance of a class. This is the realized version of a class
'''

class Shark():
    # The Constructor Method
    def __init__(self, name = 'Dolphin'):
        self.name = name

    def swimming(self):
        # Reference the name
        print(f'The {self.name} is swimming')

    def be_awesome(self):
        # Reference the name
        print(f'The {self.name} is being awesome')


def main():
    sammy = Shark('Shark')
    sammy.swimming()
    sammy.be_awesome()

if __name__ == '__main__':
    main()
