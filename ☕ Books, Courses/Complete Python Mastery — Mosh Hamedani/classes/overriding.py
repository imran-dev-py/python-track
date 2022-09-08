# Method overriding


class Animal():
    def __init__(self):
        self.age = 10

    def eat(self):
        print('eating')


class Mammal(Animal):
    def __init__(self, age):
        super().__init__()
        self.age = age
        self.weight = 20

    def eat(self):
        print('eating')


a = Animal()
m = Mammal(45)
print(isinstance(m, Mammal))
print(issubclass(Mammal, Animal))
m.eat()  # eating
print(m.age)  # 20
print(a.age)  # 10
print(m.weight)