def main():
    print("=== Coordinates Tracker ===")
    coordinates = []  

    while True:
        print("\n--- Menu ---")
        print("1) Add a coordinate (x, y)")
        print("2) View all coordinates")
        print("3) Show distance between two points")
        print("0) Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Logic to add a coordinate goes here.")

        elif choice == "2":
            print("Logic to display all coordinates goes here.")

        elif choice == "3":
            print("Logic to calculate distance between two points goes here.")

        elif choice == "0":
            print("Goodbye! 📍")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
