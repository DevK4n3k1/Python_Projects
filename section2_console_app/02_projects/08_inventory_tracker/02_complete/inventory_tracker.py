def main():
    print("=== Inventory Tracker ===")
    inventory = {}  # {item_name: quantity}

    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View inventory")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            item = input("Enter item name: ").strip().lower()
            qty = input("Enter quantity: ")

            if not qty.isdigit():
                print("Quantity must be a number.")
                continue

            qty = int(qty)

            # Add
            if item in inventory:
                inventory[item] += qty
                print(f"Updated {item}, new quantity: {inventory[item]}")
            else:
                inventory[item] = qty
                print(f"Added {item} with quantity {qty}")

        elif choice == "2":
            item = input("Enter item name to remove: ").strip().lower()
            if item in inventory:
                del inventory[item]
                print(f"Removed {item} from inventory.")
            else:
                print("Item not found.")

        elif choice == "3":
            if not inventory:
                print("Inventory is empty.")
            else:
                print("\n--- Current Inventory ---")
                for item, qty in inventory.items():
                    print(f"- {item}: {qty}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
