import os

def list_files():
    print("\n📂 File Lister")

    path = input("Enter a folder path: ")
    print(path)

def main():
    while True:
        list_files()

        choice = input("\nList another folder? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()

