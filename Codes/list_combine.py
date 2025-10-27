class cat:
    def speak(self):
        return "meow"
class dog:
    def speak(self):
        return "bark"
def animal_sound(animal):
    print(animal.speak())
animal_sound(cat())
animal_sound(dog())