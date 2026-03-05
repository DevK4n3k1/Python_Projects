class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
            
    def show_info(self):
        print(f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}")

def main():
    print("=== Contact Book ===")
    contacts = [] # list to store Contact objects Later
    
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
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            contact = Contact(name, phone, email)
            contacts.append(contact)
            print(f"Contact for {name} added.")

        elif choice == "2":
            print("View all contacts logic here")
        elif choice == "3":
            print("Search contact logic here")
        elif choice == "4":
            print("Delete contact logic here")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
