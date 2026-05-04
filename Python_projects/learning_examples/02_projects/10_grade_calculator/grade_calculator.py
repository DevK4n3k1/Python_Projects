def main():
    print("=== Grade Calculator ===")

    # Ask for a score
    score = float(input("Enter your score (0–100): "))

    # Decide grade based on score
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Your grade is: {grade}")

if __name__ == "__main__":
    main()
