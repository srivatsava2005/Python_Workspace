# Parent class
class Pirate:
    def __init__(self, name):
        self.name = name

    def sail(self):
        print(f"{self.name} is sailing the Grand Line!")

# Child class (inherits from Pirate)
class StrawHatPirate(Pirate):
    def special_move(self):
        print(f"{self.name} uses a special Straw Hat attack!")

# Create objects
luffy = StrawHatPirate("Luffy")

# Use methods
luffy.sail()          # Inherited from Pirate
luffy.special_move()  # From StrawHatPirate




#2 Example


# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting...")

# Child class (inherits from Vehicle)
class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving on the road!")

# Create an object of the child class
my_car = Car("Toyota")

# Use methods
my_car.start()   # Inherited from Vehicle
my_car.drive()   # From Car


