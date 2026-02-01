import csv
from datetime import date

FILE_NAME = "attendance.csv"

def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Status"])
    except FileExistsError:
        pass

def mark_attendance():
    name = input("Enter student name: ").strip()
    status = input("Enter status (Present/Absent): ").strip().capitalize()

    if not name or status not in ["Present", "Absent"]:
        print("❌ Invalid input.")
        return

    today = date.today().isoformat()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, today, status])

    print("✅ Attendance recorded.")

def view_attendance():
    print("\n📋 Attendance Records")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No attendance records found.")

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
