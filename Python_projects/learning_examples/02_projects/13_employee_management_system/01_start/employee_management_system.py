class Employee:
    def __init__(self, name, emp_id, salary):
        print("Initialize base Employee fields here")

    def show_info(self):
        print("Display Employee info here")


class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        print("Initialize Manager fields here (and call base init)")

    def show_info(self):
        print("Display Manager info here (and call base show_info)")


class Developer(Employee):
    def __init__(self, name, emp_id, salary, language):
        print("Initialize Developer fields here (and call base init)")

    def show_info(self):
        print("Display Developer info here (and call base show_info)")

def main():
    print("=== Employee Management System ===")
    employees = []  # will store Employee/Manager/Developer objects later

    while True:
        print("\nOptions:")
        print("1) Add Manager")
        print("2) Add Developer")
        print("3) View all employees")
        print("4) Search employee by ID")
        print("5) Quit")

        choice = input("Enter 1-5: ")

        if choice == "1":
            print("Collect manager details and append a Manager object here")

        elif choice == "2":
            print("Collect developer details and append a Developer object here")

        elif choice == "3":
            print("Loop through employees and display info here")

        elif choice == "4":
            print("Ask for ID, search the list, and show matching employee here")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
