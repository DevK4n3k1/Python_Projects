##############################################
# Indexing
##############################################
fruits = ["apple", "banana", "cherry", "orange"]

print(fruits[0])   # Output: apple
print(fruits[1])   # Output: banana
print(fruits[2])   # Output: cherry
print(fruits[3])   # Output: orange

print(fruits[-1])  # Output: orange (last item)
print(fruits[-2])  # Output: cherry (second last)


##############################################
# Slicing
##############################################
fruits = ["apple", "banana", "cherry", "orange", "grape"]
print(fruits[1:4])

print(fruits[:3])   # ['apple', 'banana', 'cherry']
print(fruits[2:])   # ['cherry', 'orange', 'grape']

print(fruits[0:5:2])  # ['apple', 'cherry', 'grape']


##############################################
# Adding Items
##############################################
# append() 
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  


# insert()
fruits.insert(1, "grape")
print(fruits)

# extend()
fruits.extend(["kiwi", "melon"])
print(fruits)


##############################################
# Changing Items
##############################################
fruits = ["apple", "banana", "cherry", "orange"]
fruits[1] = "grape"
print(fruits)

fruits[1:3] = ["kiwi", "melon"]
print(fruits)


##############################################
# Removing Items
##############################################
# remove()
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)

# pop()
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)

fruits.pop()
print(fruits)

# del
fruits = ["apple", "banana", "cherry"]
del fruits[0]
print(fruits)

fruits = ["apple", "banana", "cherry", "orange"]
del fruits[1:3]
print(fruits)

# clear()
fruits.clear()
print(fruits)


##############################################
# Loop through a list
##############################################
# for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
