# =====================================================
# POLYMORPHISM IN PYTHON - FULL CODE (SINGLE FILE)
# =====================================================

# Polymorphism = "Many forms"
# Same method name behaves differently for different objects


# =====================================================
# 1. BASIC POLYMORPHISM (Same method name, different classes)
# =====================================================

class Dog:
    def speak(self):
        return "Dog says: Woof!"

class Cat:
    def speak(self):
        return "Cat says: Meow!"

class Cow:
    def speak(self):
        return "Cow says: Moo!"


# Function that works with any object having speak() method
def make_animal_speak(animal):
    print(animal.speak())


# Creating objects
dog = Dog()
cat = Cat()
cow = Cow()

print("---- BASIC POLYMORPHISM ----")
make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(cow)


# =====================================================
# 2. DUCK TYPING (Python doesn't care about class type)
# =====================================================
# If an object has the needed method, Python will use it.

class Car:
    def move(self):
        return "Car is driving"

class Boat:
    def move(self):
        return "Boat is sailing"

class Plane:
    def move(self):
        return "Plane is flying"


def start_vehicle(vehicle):
    # Works for ANY object having move() method
    print(vehicle.move())


print("\n---- DUCK TYPING ----")
start_vehicle(Car())
start_vehicle(Boat())
start_vehicle(Plane())


# =====================================================
# 3. POLYMORPHISM USING INHERITANCE + METHOD OVERRIDING
# =====================================================

class Shape:
    # Parent class method
    def area(self):
        return "Area formula not defined"


class Rectangle(Shape):
    # Child class overriding parent method
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    # Child class overriding parent method
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius * self.radius


print("\n---- METHOD OVERRIDING ----")
rect = Rectangle(10, 5)
circle = Circle(7)

print("Rectangle area:", rect.area())
print("Circle area:", circle.area())


# =====================================================
# 4. POLYMORPHISM IN FUNCTIONS (same operator, different meaning)
# =====================================================

print("\n---- OPERATOR POLYMORPHISM ----")

print(10 + 5)         # Integer addition
print("Hello" + " World")  # String concatenation
print([1, 2] + [3, 4])     # List merging


# =====================================================
# 5. POLYMORPHISM WITH ABSTRACT BASE CLASSES
# =====================================================

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Lion(Animal):
    def sound(self):
        return "Lion roars"

class Snake(Animal):
    def sound(self):
        return "Snake hisses"


print("\n---- ABSTRACT CLASS POLYMORPHISM ----")

animals = [Lion(), Snake()]

for animal in animals:
    print(animal.sound())


# =====================================================
# FINAL MESSAGE
# =====================================================

print("\n✅ This single file demonstrated:")
print("1. Method polymorphism")
print("2. Duck typing")
print("3. Method overriding")
print("4. Operator polymorphism")
print("5. Abstract class polymorphism")
