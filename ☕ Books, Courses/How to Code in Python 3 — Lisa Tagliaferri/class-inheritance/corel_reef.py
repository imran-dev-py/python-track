class Coral():
    def community(self):
        print('Coral Lives in community')

class Anemone():
    def protect_clownfish(self):
    print("The anemone is protecting the clownfish.")

    def community(self):
    print('ClownFish Lives in community')

'''
If the same method is defined in multiple parent methods,
the child class will use the method of the first parent declared in its tuple list.
'''
class CoralReef(Coral, Anemone):
    pass

great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()
