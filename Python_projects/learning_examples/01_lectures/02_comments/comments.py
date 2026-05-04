##############################################
# Single-Line Comments
##############################################
# This is a comment
print("Hello, World!")  # This prints a message


##############################################
# Multi-Line Comments 
##############################################
"""
This is a multi-line comment.
It can span multiple lines.
Python ignores everything inside these triple quotes.
"""
print("Hello, World!")


##############################################
# Commenting Out for Debugging
##############################################
def add_numbers(a, b):
    sum_result = a + b
    print("Sum:", sum_result)
    print("Multiplication:", a * b)  # This line is unnecessary for addition

add_numbers(5, 3)

