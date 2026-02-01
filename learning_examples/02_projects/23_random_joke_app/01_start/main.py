import requests

def get_random_joke():
    pass

def main():
    while True:
        get_random_joke()

        choice = input("\nGet another joke? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()

