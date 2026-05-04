def main():
    print("=== Coordinates Tracker ===")
    coordinates = []

    while True:
        print("\n--- Menu ---")
        print("1) Add a coordinate (x, y)")
        print("2) View all coordinates")
        print("3) Show distance between two points")
        print("0) Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            x = float(input("Enter x: "))
            y = float(input("Enter y: "))
            point = (x, y)
            coordinates.append(point)
            print(f"Point {point} added.")

        elif choice == "2":
            if not coordinates:
                print("No coordinates saved yet.")
            else:
                print("Saved coordinates:")
                for i, (x, y) in enumerate(coordinates, start=1):
                    print(f"{i}. ({x}, {y})")

        elif choice == "3":
            if len(coordinates) < 2:
                print("You need at least 2 points to calculate distance.")
            else:
                for i, (x, y) in enumerate(coordinates, start=1):
                    print(f"{i}. ({x}, {y})")

                i1 = int(input("Choose first point number: ")) - 1
                i2 = int(input("Choose second point number: ")) - 1

                x1, y1 = coordinates[i1]
                x2, y2 = coordinates[i2]

                # Distance formula
                dist = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
                print(f"Distance between {coordinates[i1]} and {coordinates[i2]} = {dist:.2f}")

        elif choice == "0":
            print("Goodbye! 📍")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()