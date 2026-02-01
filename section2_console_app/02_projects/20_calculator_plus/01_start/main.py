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
    
    # Logic

def main():
    while True:
        calculator_plus()

        again = input("\nUse calculator again? (y/n): ").lower()
        if again != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()

