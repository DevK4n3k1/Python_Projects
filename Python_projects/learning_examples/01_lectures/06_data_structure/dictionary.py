##############################################
# Basics
##############################################
# Accessing Values
my_dict = {
    "apple": "a sweet fruit",
    "banana": "a yellow fruit"
}

print(my_dict["apple"])


# print(my_dict["grape"]) # Error
print(my_dict.get("grape"))
print(my_dict.get("grape", "Not found"))


##############################################
# Adding or Changing Items
##############################################
student = {
    "name": "Alice",
    "age": 20
}

# Adding Items
student["major"] = "Computer Science"
print(student)

# Changing Items
student["age"] = 21
print(student)


##############################################
# Removing Items 
##############################################
student = {
    "name": "Alice",
    "age": 20,
    "major" : "Computer Science"
}

# pop()
student.pop("age")
print(student)

# del
del student["name"]
print(student)

# clear()
student.clear()
print(student)


##############################################
# Looping Through a Dictionary
##############################################
my_dict = {
    "name": "Alice",
    "age": 20
}

# Keys
for key in my_dict.keys():
    print(key)

# for key in my_dict:
#     print(key)


# Values
for value in my_dict.values():
    print(value)

# Key-Value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")


