def main():
    print("=== Shopping List App ===")
    shopping_list = []

    while True:
        print("\n--- Menu ---")
        print("1) Add item")
        print("2) View list")
        print("3) Remove item")
        print("0) Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter an item to add: ")
            shopping_list.append(item)
            print(item, "added to the list.")

        elif choice == "2":
            if len(shopping_list) == 0:
                print("Your shopping list is empty.")
            else:
                print("Your shopping list:")
                for i in range(len(shopping_list)):
                    print(str(i + 1) + ". " + shopping_list[i])

        elif choice == "3":
            if len(shopping_list) == 0:
                print("Your list is empty. Nothing to remove.")
            else:
                item = input("Enter the item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(item, "removed from the list.")
                else:
                    print(item, "not found in the list.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
