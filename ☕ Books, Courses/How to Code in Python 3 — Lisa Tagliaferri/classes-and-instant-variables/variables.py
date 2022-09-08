'''
At the class level, variables are referred to as class variables,
whereas variables at the instance level are called instance variables.
'''

# Class Variables
class Shark():
    animal_type = 'Fish'
    location = 'Ocean'
    followers = 5

    def __init__(self, name):
        self.name = name

    def about_shark(self):
        print(f'The {self.name} what kind of Animal? {self.animal_type}')
        print(f'How many followers he has? {self.followers}')
        print(f'Where the {self.name} live? {self.location}')

new_shark = Shark('Shark')
new_shark.about_shark()

print()
# Instance Variables
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

new_shark = Shark("Sammy", 5)
print(new_shark.name)
print(new_shark.age)

# Working with Class and Instance Variables Together
print()

class Dolphin():
    # class variable
    animal_type = 'Fish'
    location = 'Ocean'

    # Constructor method with instance variables
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_followers(self, followers):
        return f'The user has {followers} followers'

def main():
    print('1st Object')
    # First object
    little_dolphin = Dolphin('Sammy', 5)
    # Instance variable name
    print(little_dolphin.name)
    # Class variable location
    print(little_dolphin.location)

    print()
    print('2nd Object')
    # 2nd object
    little_dolphin_2 = Dolphin('Stevie', 4)
    # Instance Variable name
    print(little_dolphin_2.name);
    # Use set followers method and pass instance variable followers
    print(little_dolphin_2.set_followers(55))

    # Class Variable animal type
    print(little_dolphin.animal_type)

if __name__ == '__main__':
    main()
