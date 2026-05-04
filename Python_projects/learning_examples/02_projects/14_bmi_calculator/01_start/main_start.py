def calculate_bmi():
    print("\n--- BMI Calculator ---")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    bmi = weight / (height ** 2)
    print(f"\nYour BMI is: {bmi:.2f}")

def main():
    while True:
        calculate_bmi()

        choice = input("\nCalculate again? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()

