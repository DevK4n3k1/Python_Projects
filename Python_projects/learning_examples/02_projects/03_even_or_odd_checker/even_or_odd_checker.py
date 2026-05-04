def main():
    print("=== Even or Odd Checker ===")

    number = int(input("Enter an integer: "))

    if number % 2 == 0:
        print(f"{number} is Even ✅")
    else:
        print(f"{number} is Odd 🔢")

if __name__ == "__main__":
    main()
