##############################################
# Basics
##############################################
fruits = ["apple", "banana", "grape"]

for fruit in fruits:
    print(f"This is {fruit}")



##############################################
# Loop Numbers
##############################################
for i in range(1, 6):
    print(i)



##############################################
# Loop Strings
##############################################
for letter in "Python":
    print(letter)



##############################################
# Break
##############################################
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)


##############################################
# Continue
##############################################
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

