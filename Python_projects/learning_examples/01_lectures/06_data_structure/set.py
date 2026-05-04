##############################################
# Basics
##############################################
my_set = {"apple", "banana", "apple"}

# Unique Item Only
print(my_set)

# Adding items
my_set.add("orange")

# Removing items 
my_set.remove("banana")

# Looping
for item in my_set:
    print(item)


# CAN'T
# print(my_set[0])    # Indexing
# print(my_set[1:2])  # Slicing


##############################################
# Math Operations
##############################################
# Union (A ∪ B)
basket1 = {"apple", "banana"}
basket2 = {"banana", "cherry"}
result = basket1.union(basket2)
print(result)


# Intersection (A ∩ B) 
result = basket1.intersection(basket2)
print(result)


# Difference (A - B) 
result = basket1.difference(basket2)
print(result)

# Symmetric Difference
result = basket1.symmetric_difference(basket2)
print(result)
