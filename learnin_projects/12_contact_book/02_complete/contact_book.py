class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def show_info(self):
        print(f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}")

def main():
    print("=== Contact Book ===")
    contacts = []  # list to store Contact objects

    while True:
        print("\nOptions:")
        print("1) Add contact")
        print("2) View all contacts")
        print("3) Search contact")
        print("4) Delete contact")
        print("5) Quit")

        choice = input("Enter 1-5: ")

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            contact = Contact(name, phone, email)
            contacts.append(contact)
            print(f"Contact for {name} added.")

        elif choice == "2":
            if not contacts:
                print("No contacts found.")
            else:
                print("\n--- All Contacts ---")
                for c in contacts:
                    c.show_info()

        elif choice == "3":
            search_name = input("Enter name to search: ").strip().lower()
            found = False
            for c in contacts:
                if c.name.lower() == search_name:
                    c.show_info()
                    found = True
            if not found:
                print("Contact not found.")

        elif choice == "4":
            del_name = input("Enter name to delete: ").strip().lower()
            for c in contacts:
                if c.name.lower() == del_name:
                    contacts.remove(c)
                    print(f"Contact {c.name} deleted.")
                    break
            else:
                print("Contact not found.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
