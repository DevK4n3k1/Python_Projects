##############################################
# Basics
##############################################
# Indexing
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
print(fruits[-1]) # cherry

# Slicing
print(fruits[0:2])  # ('apple', 'banana')

# Looping
for fruit in fruits:
    print(fruit)


# CAN'T
# fruits[1] = "grape"      # Error: Tuples can't be changed
# fruits.append("orange")  # Error: No append method
# fruits.remove("apple")   # Error: No remove method

