import time

def countdown_timer():
    print("\n⏳ Countdown Timer")
    seconds = int(input("Enter time in seconds: "))
    print(seconds)

def main():
    while True:
        countdown_timer()

        choice = input("\nStart another timer? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()

