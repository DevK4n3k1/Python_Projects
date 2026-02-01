##############################################
# Basic try…except
##############################################
try:
    number = int(input("Enter a number: "))
    print("You typed:", number)
except ValueError:
    print("That wasn't a number. Please try again.")


##############################################
# try…except (catch all errors)
##############################################
try:
    result = 10 / int(input("Enter a divisor: "))
    print("Result:", result)
except Exception as e:
    print("Oops! Something went wrong:", e)


##############################################
# try…except…else
##############################################
try:
    n = int(input("Enter a number: "))
except ValueError:
    print("That wasn't a number.")
else:
    print("You entered:", n)  # runs only if no error


##############################################
# try…except…finally
##############################################
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Not a number!")
finally:
    print("Thanks for trying!")  # always runs

