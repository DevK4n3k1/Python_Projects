import time

def countdown_timer():
    print("\n⏳ Countdown Timer")

    try:
        seconds = int(input("Enter time in seconds: "))

        if seconds <= 0:
            print("Please enter a positive number.")
            return

        while seconds > 0:
            print(f"Time remaining: {seconds} seconds")
            time.sleep(1)
            seconds -= 1

        print("⏰ Time's up!")

    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    while True:
        countdown_timer()

        choice = input("\nStart another timer? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()

