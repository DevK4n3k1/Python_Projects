def main():
    print("=== Inventory Tracker ===")
    inventory = {}  # this will store items and their quantities

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View inventory")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print("Add item logic here")

        elif choice == "2":
            print("Remove item logic here")

        elif choice == "3":
            print("View inventory logic here")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
