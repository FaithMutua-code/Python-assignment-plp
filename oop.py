'''
Create a program that includes animals or vehicles with the same action (like move()).
 However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, 
 while Plane.move() prints "Flying" ✈️).
'''
# Define the Car class
class Car:
    def move(self):
        print("Driving 🚗")

# Define the Plane class
class Plane:
    def move(self):
        print("Flying ✈️")

# Define the Dog class
class Dog:
    def move(self):
        print("Running 🐕")

# Define the Fish class
class Fish:
    def move(self):
        print("Swimming 🐟")

# Create a list of objects
things_that_move = [Car(), Plane(), Dog(), Fish()]

# Loop through the list and call move() on each one
for thing in things_that_move:
    thing.move()
