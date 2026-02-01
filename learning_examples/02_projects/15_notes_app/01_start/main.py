FILE_NAME = "notes.txt"

def view_notes():
    pass

def add_note():
    pass

def main():
    while True:
        print("\n===================")
        print(" Simple Notes App")
        print("===================")
        print("1. View notes")
        print("2. Add note")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            view_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

