##############################################
# Arithmetic Operators
##############################################
a = 10
b = 3

print("Addition:", a + b)        # 10 + 3 = 13
print("Subtraction:", a - b)     # 10 - 3 = 7
print("Multiplication:", a * b)  # 10 * 3 = 30
print("Division:", a / b)        # 10 / 3 = 3.333...
print("Modulus:", a % b)         # 10 % 3 = 1
print("Exponentiation:", a ** b) # 10 ** 3 = 1000
print("Floor Division:", a // b) # 10 // 3 = 3


##############################################
# Comparison Operators
##############################################
a = 10
b = 3

print("a == b:", a == b)         # False
print("a != b:", a != b)         # True
print("a > b:", a > b)           # True
print("a < b:", a < b)           # False
print("a >= b:", a >= b)         # True
print("a <= b:", a <= b)         # False


##############################################
# Logical Operators
##############################################
a = 10
b = 3

print("a > 5 and b < 5:", a > 5 and b < 5)    # True and True → True
print("a < 5 or b < 5:", a < 5 or b < 5)      # False or True → True
print("not(a > 5):", not(a > 5))              # not True → False


##############################################
# Assignment Operators
##############################################
# =  Assign
x = 5
print("x = 5 →", x)              # 5

# +=  Add and assign
x += 3
print("x += 3 →", x)             # 5 + 3 = 8

# -=  Subtract and assign
x -= 2
print("x -= 2 →", x)             # 8 - 2 = 6

# *=  Multiply and assign
x *= 2
print("x *= 2 →", x)             # 6 * 2 = 12

# /=  Divide and assign
x /= 3
print("x /= 3 →", x)             # 12 / 3 = 4.0

# //=  Floor divide and assign
x //= 2
print("x //= 2 →", x)            # 4.0 // 2 = 2.0

# %=  Modulus and assign
x %= 2
print("x %= 2 →", x)             # 2.0 % 2 = 0.0

# **=  Power and assign
x = 2
x **= 3
print("x **= 3 →", x)            # 2 ** 3 = 8


##############################################
# Membership Operators
##############################################
fruits = ['apple', 'orange', 'grape']

print('apple' in fruits)          # True
print('banana' not in fruits)     # True

# With strings
message = "Welcome to Python"
print('Python' in message)        # True
print('Java' not in message)      # True



##############################################
# Identity Operators
##############################################
a = [1, 2, 3]
b = a               # b points to the same list as a
c = [1, 2, 3]

print(a is b)       #Output: True
print(a is not c)   #Output: True

# Check memory addresses
print(id(a))  # Same as id(b)
print(id(b))  # Same as id(a)
print(id(c))  # Different from a and b