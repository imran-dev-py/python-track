class Shark():
    # The Constructor Method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        # Reference the name
        print(f'The {self.name} is {self.age} and it can swim')

    def be_awesome(self):
        # Reference the name
        print(f'The {self.name} is {self.age} and going to be awesome')


def main():
    sammy = Shark('Shark', 3)
    sammy.swimming()
    steive = Shark('Dolphin', 5)
    steive.be_awesome()

if __name__ == '__main__':
    main()
