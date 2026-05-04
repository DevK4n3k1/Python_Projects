##############################################
# Inheritance
##############################################
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"{self.color} {self.brand} engine started.")

    def honk(self):
        print(f"{self.brand} says 'Beep beep!'")


class ElectricCar(Car):  # Inheriting from Car
    def charge_battery(self):
        print(f"{self.brand} is charging the battery.")

my_electric_car = ElectricCar("Tesla", "White")

my_electric_car.start_engine()      # Inherited from Car
my_electric_car.honk()              # Inherited from Car
my_electric_car.charge_battery()    # Unique to ElectricCar


##############################################
# Override
##############################################
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"{self.color} {self.brand} engine started.")

class ElectricCar(Car):
    def start_engine(self):  # Overriding the parent method
        print(f"{self.brand} starts silently. No engine noise.")
        
tesla = ElectricCar("Tesla", "White")
tesla.start_engine()   # Tesla starts silently. No engine noise.