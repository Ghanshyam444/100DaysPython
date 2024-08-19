# Single Inheritance

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by animal")

    
class Dog(Animal):
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("Bark!")
        
d = Dog("Tommy","Pug")
d.make_sound()

a = Animal("Dog","Dog")
a.make_sound()

# Quick Quiz : Implement a cat class by using animal class. Add some methods specific to cat class.