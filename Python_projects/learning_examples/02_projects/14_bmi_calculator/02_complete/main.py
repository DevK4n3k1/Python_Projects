def calculate_bmi():
    print("\n--- BMI Calculator ---")

    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0:
            raise ValueError("Weight must be a positive number.")
        if height < 0:
            raise ValueError("Height must be a positive number.")
        if height == 0:
            raise ZeroDivisionError

        bmi = weight / (height ** 2)
        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

    except ValueError as e:
        print(f"❌ ValueError: {e}")
    except ZeroDivisionError:
        print("❌ ZeroDivisionError: Height cannot be zero.")

def main():
    while True:
        calculate_bmi()

        choice = input("\nCalculate again? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()

