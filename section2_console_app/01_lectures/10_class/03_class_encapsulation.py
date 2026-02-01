##############################################
# Encapsulation
##############################################
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed  # Private attribute

    # Getter
    def get_speed(self):
        return self.__speed

    # Setter
    def set_speed(self, speed):
        self.__speed = speed
        

my_car = Car("Toyota", 100)

print(my_car.get_speed())  # Output: 100

my_car.set_speed(120)      # Update speed safely
print(my_car.get_speed())  # Output: 120

# print(my_car.__speed)  # Error: AttributeError
