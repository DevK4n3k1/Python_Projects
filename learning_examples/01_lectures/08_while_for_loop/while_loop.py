##############################################
# Basics
##############################################
count = 1
while count <= 5:
    print(count)
    count += 1

# while True:
#     print("This will run forever")


##############################################
# Break
##############################################
num = 1
while True:
    print(num)
    if num == 3:
        break  # Stop the loop when num is 3
    num += 1


##############################################
# Continue
##############################################
num = 0

while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)


##############################################
# Else
##############################################
x = 1
while x <= 3:
    print(x)
    x += 1
else:
    print("Loop finished!")
    
    

# x = 1
# while x <= 3:
#     print(x)
#     if x == 2:
#         break
#     x += 1
# else:
#     print("Loop finished!")  # This won't print
