class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def show_info(self):
        print(f"ID: {self.emp_id} | Name: {self.name} | Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size

    def show_info(self):
        super().show_info()
        print(f"  Role: Manager | Team size: {self.team_size}")

class Developer(Employee):
    def __init__(self, name, emp_id, salary, language):
        super().__init__(name, emp_id, salary)
        self.language = language

    def show_info(self):
        super().show_info()
        print(f"  Role: Developer | Language: {self.language}")

def main():
    print("=== Employee Management System ===")
    employees = []  # list to store Employee objects

    while True:
        print("\nOptions:")
        print("1) Add Manager")
        print("2) Add Developer")
        print("3) View all employees")
        print("4) Search employee by ID")
        print("5) Quit")

        choice = input("Enter 1-5: ")

        if choice == "1":
            name = input("Enter manager name: ")
            emp_id = input("Enter employee ID: ")
            salary = input("Enter salary: ")
            team_size = input("Enter team size: ")
            manager = Manager(name, emp_id, salary, team_size)
            employees.append(manager)
            print(f"Manager {name} added.")

        elif choice == "2":
            name = input("Enter developer name: ")
            emp_id = input("Enter employee ID: ")
            salary = input("Enter salary: ")
            language = input("Enter primary programming language: ")
            developer = Developer(name, emp_id, salary, language)
            employees.append(developer)
            print(f"Developer {name} added.")

        elif choice == "3":
            if not employees:
                print("No employees found.")
            else:
                print("\n--- All Employees ---")
                for emp in employees:
                    emp.show_info()

        elif choice == "4":
            search_id = input("Enter employee ID to search: ")
            found = False
            for emp in employees:
                if emp.emp_id == search_id:
                    emp.show_info()
                    found = True
                    break
            if not found:
                print("Employee not found.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
