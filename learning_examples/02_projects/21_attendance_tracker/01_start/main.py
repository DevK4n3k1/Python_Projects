import csv
from datetime import date

FILE_NAME = "attendance.csv"

def initialize_file():
    pass
def mark_attendance():
    pass
def view_attendance():
    pass

def main():
    initialize_file()

    while True:
        print("\n==========================")
        print(" Attendance Tracker")
        print("==========================")
        print("1. Mark attendance")
        print("2. View attendance")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()

