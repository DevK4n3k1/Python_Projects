##############################################
# Basics
##############################################
# class Name:
#     def __init__(self, data):   # Constructor
#         self.param1 = data      # Attribute

#     def method(self):           # Method
#         print(self.data)


##############################################
# Example
##############################################
class Car:
    def __init__(self, brand, color):
        # Attributes
        self.brand = brand
        self.color = color

    # Method (Action)
    def start_engine(self):
        print(f"{self.color} {self.brand} engine started.")

    def honk(self):
        print(f"{self.brand} says 'Beep beep!'")
        
        
##############################################
# Create a Car Object (Instance)
##############################################
my_car = Car("Toyota", "Red")  # Creates a red Toyota
my_car.start_engine()          # Output: Red Toyota engine started.
my_car.honk()                  # Output: Toyota says 'Beep beep!'


car1 = Car("Toyota", "Red")
car2 = Car("Tesla", "White")
car3 = Car("BYD", "Silver")

car1.start_engine()
car2.start_engine()
car3.start_engine()


##############################################
# Class Variablea vs Instance Variables
##############################################
class Car:
    wheels = 4      # Class Variable (Shared)

    def __init__(self, brand, color):
        # Instance Variables (Unique to each object)
        self.brand = brand
        self.color = color

    def describe(self):
        print(f"{self.color} {self.brand} has {Car.wheels} wheels.")

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

car1.describe()  # Output: Red Toyota has 4 wheels.
car2.describe()  # Output: Blue Honda has 4 wheels.