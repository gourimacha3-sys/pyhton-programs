class Animal:
    def sound(self):
        pass
    
class cat(Animal):
    def sound(self):
        print("Meow")
        
class dog(Animal):
    def sound(self):
        print("woolf")

def make_sound(Animal):
    Animal.sound()

cat=cat()
dog=dog()
make_sound(cat)
make_sound(dog)
