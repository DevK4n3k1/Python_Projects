##############################################
# Casting to Integer
##############################################
# Decimal Number (Float) --> Integer
num = int(3.9)
print(num)  # Output: 3


# String --> Integer
# num_str = "10"
# print(num_str + 5)  # Error! Why? Because "10" is text, and 5 is a number.

num = int("10")
print(num + 5)  # Output: 15


# Boolean --> Integer
print(int(True))  # Output: 1
print(int(False)) # Output: 0


##############################################
# Casting to Float
##############################################
# Integer --> Float
num = float(5)
print(num)  # Output: 5.0


##############################################
# Casting to String
##############################################
# Number --> String
num = 25
text = str(num)

print(text)
print(type(text)) # Output: <class 'str'>


# Error
age = 30
# message = "I am " + age + " years old."     # Error! Python doesn’t allow mixing numbers and text directly.
# print(message)

# Solution
message = "I am " + str(age) + " years old."
print(message)  


##############################################
# Casting to Boolean
##############################################
# Numbers --> Boolean
print(bool(1))  # Output: True
print(bool(100)) # Output: True
print(bool(-1))  # Output: True
print(bool(0))  # Output: False


# Strings --> Boolean
print(bool("Hello"))  # Output: True
print(bool(""))       # Output: False (empty string)
print(bool(" "))      # Output: True (even a space is considered True)


##############################################
# Casting to List
##############################################
# Tuple --> List
my_tuple = (1, 2, 3)
my_list = list(my_tuple)

print(my_list)  # Output: [1, 2, 3]


my_list.append(4)  # Adds 4 to the list
print(my_list)     # Output: [1, 2, 3, 4]


# String --> List
word = "hello"
letters = list(word)

print(letters)  # Output: ['h', 'e', 'l', 'l', 'o']


# Set --> List
my_set = {10, 20, 30}
my_list = list(my_set)

print(my_list)  # Output: [10, 20, 30] (Order may vary)


##############################################
# Casting to Tuple
##############################################
# List --> Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

print(my_tuple)  # Output: (1, 2, 3)

# my_tuple.append(4)  # Error! Tuples don’t support append()


# String --> Tuple
word = "Python"
letters = tuple(word)

print(letters)  # Output: ('P', 'y', 't', 'h', 'o', 'n')


# Set --> Tuple
my_set = {10, 20, 30}
my_tuple = tuple(my_set)

print(my_tuple)  # Output: (10, 20, 30) (Order may vary)



##############################################
# Casting to Set
##############################################
# List --> Set
my_list = [1, 2, 2, 3, 3, 4]
my_set = set(my_list)

print(my_set)  # Output: {1, 2, 3, 4}


# Keep Order But Remove Duplicates
my_list = [8, 3, 8, 7, 3, 5]
unique_list = list(dict.fromkeys(my_list))

print(unique_list)  # Output: [8, 3, 7, 5]

