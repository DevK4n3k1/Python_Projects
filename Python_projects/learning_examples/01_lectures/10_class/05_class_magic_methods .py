##############################################
# Magic Methods 
##############################################
# __init__() and __str__()
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"{self.color} {self.brand}"

my_car = Car("Toyota", "Red")
print(my_car)



# __len__()
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __len__(self):
        return len(self.brand) + len(self.color)

my_car = Car("Toyota", "Red")
print(len(my_car))  # Output: 9 (6 + 3)
