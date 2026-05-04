import os

def list_files():
    print("\n📂 File Lister")

    path = input("Enter a folder path: ")

    try:
        items = os.listdir(path)

        if not items:
            print("The folder is empty.")
            return

        print("\nContents:")
        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                print(f"[FILE]   {item}")
            else:
                print(f"[FOLDER] {item}")

    except FileNotFoundError:
        print("❌ Folder not found. Please check the path.")

def main():
    while True:
        list_files()

        choice = input("\nList another folder? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()
