##############################################
# Basics
##############################################
text = "Python"

# Indexing
print(text[0])  # 'P'
print(text[-1]) # 'n'  last character

# Slicing
print(text[0:3])    # 'Pyt'
print(text[2:])     # 'thon'
print(text[:4])     # 'Pyth'

# Looping
for char in text:
    print(char)


##############################################
# String Methods
##############################################
# Sample string to work with
text = "  Hello, Python 123!  "

# 1. lower()
print(text.lower())

# 2. upper()
print(text.upper())

# 3. strip()
print(text.strip())

# 4. replace()
print(text.replace("Python", "World"))

# 5. split()
print(text.strip().split(" "))

# 6. join()
words = ["apple", "banana", "cherry"]
print(", ".join(words))

# 7. startswith()
print(text.strip().startswith("Hello"))

# 8. endswith()
print(text.strip().endswith("123!"))

# 9. isalpha()
print("Hello".isalpha())

# 10. isdigit()
print("123".isdigit())

# 11. find()
print(text.find("Python"))









