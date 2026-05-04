##############################################
# Polymorphism
##############################################
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Bird:
    def speak(self):
        print("Tweet!")


animals = [Dog(), Cat(), Bird()]

for animal in animals:
    animal.speak()  # Same method, different output



##############################################
# Polymorphism with Inheritance
##############################################
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()
