##############################################
# Basics
##############################################
def greet():
    print("Hello! Welcome to Python.")

greet()


##############################################
# Functions with Parameters
##############################################
def greet(name):
    print(f"Hello, {name}!")

greet("Tom")
greet("Alice")
greet("Bob")


##############################################
# Functions with Return Value
##############################################
def add(a, b):
    return a + b

result = add(3, 5)
print(result)


