from datetime import date

def calculate_age():
    print("\n🎂 Age Calculator")
    year = int(input("Enter birth year (YYYY): "))
    month = int(input("Enter birth month (1-12): "))
    day = int(input("Enter birth day (1-31): "))

    print(f"\nYou are -- years old.")

def main():
    while True:
        calculate_age()

        choice = input("\nCalculate again? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()

