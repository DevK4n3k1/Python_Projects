import math

def calculator_plus():
    print("\n🧮 Calculator Plus")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")

    choice = input("Choose an operation (1-6): ")

    try:
        if choice in ["1", "2", "3", "4"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", a + b)

            elif choice == "2":
                print("Result:", a - b)

            elif choice == "3":
                print("Result:", a * b)

            elif choice == "4":
                print("Result:", a / b)

        elif choice == "5":
            num = float(input("Enter a number: "))
            if num < 0:
                print("❌ Cannot calculate square root of a negative number.")
            else:
                print("Result:", math.sqrt(num))

        elif choice == "6":
            base = float(input("Enter base: "))
            exp = float(input("Enter exponent: "))
            print("Result:", math.pow(base, exp))

        else:
            print("❌ Invalid choice.")

    except ZeroDivisionError:
        print("❌ Error: Division by zero is not allowed.")
    except ValueError:
        print("❌ Error: Please enter valid numbers.")

def main():
    while True:
        calculator_plus()

        again = input("\nUse calculator again? (y/n): ").lower()
        if again != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()
