FILE_NAME = "notes.txt"

def view_notes():
    print("\n--- Your Notes ---")
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if content.strip() == "":
                print("No notes yet.")
            else:
                print(content)
    except FileNotFoundError:
        print("No notes file found. Add a note first.")


def add_note():
    note = input("\nEnter your note: ")

    if note.strip() == "":
        print("Note cannot be empty.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note saved successfully.")


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
