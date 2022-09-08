'''
What is Inheritance — Inheritance means when a class uses code constructed within
another class...
'''
# Super class [Parent Class]
class Fish():
    def __init__(self, first_name, last_name = 'Fish', skeleton = 'bone', eyelids = False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print('The Fish is swimming')

    def backwards_swim(self):
        print('The fish can swim backwards')


# Sub class [Child Class]
class Trout(Fish):
    def __init__(self, water = 'freshwater'):
        self.water = water
        super().__init__(self)

terry = Trout()
terry.first_name = "Trout"
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.backwards_swim()
print(f'{terry.first_name} {terry.last_name} lives in {terry.water}')

# another sub class
class ClownFish(Fish):
    def live_with_anemone(self):
        print('The clownfish is coexisting with sea anemone')

casey = ClownFish('casey')
print(casey.first_name +" "+casey.last_name)
casey.swim()
casey.live_with_anemone()

# Overriding Parent Methods
print()

class Shark(Fish):
    def __init__(self, last_name ='Shark', skeleton ='cartilage', eyelids = True):
        super().__init__(self)
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    # Overridden method from class
    def overriden_method(self):
        super().backwards_swim()

    def backwards_swim(self):
        print('The shark cannot swim backwards, but can sink backwards')

sammy = Shark()
# sammy = Shark('Sammy')
sammy.first_name = 'Sammy'
print(sammy.first_name +" "+sammy.last_name)
sammy.swim()
sammy.backwards_swim()
print(sammy.skeleton)
print(sammy.eyelids)
sammy.overriden_method()
