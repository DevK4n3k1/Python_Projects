def main():
    print("=== Shopping List Cleaner ===")

    text = input("Enter your shopping list items separated by commas:\n> ")

    # Split by commas, strip spaces, and lowercase for consistency
    items = [item.strip().lower() for item in text.split(',') if item.strip()]

    # Use set() to remove duplicates
    unique_items = sorted(set(items))  # sorted alphabetically

    print("\n--- Cleaned Shopping List ---")
    print("Total items entered:", len(items))
    print("Unique items:", len(unique_items))

    print("Your cleaned list")
    for item in unique_items:
        print("-", item)

if __name__ == "__main__":
    main()
