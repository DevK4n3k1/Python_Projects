def main():
    print("*** Even or Odd Checker ***")

    while True:
        try:
            number = int(input("Enter an number: "))
            break
        except ValueError:
            print("❌ That's not a valid integer. Please try again.")


    if number % 2 == 0:
        print(f"{number} is Even ✅") 
    else:
        print(f"{number} is Odd 🔢")

if __name__ == "__main__":
    main() 