import requests

API_KEY = "YOUR_API_KEY_HERE"   # ← put your API key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def check_weather():
    pass

def main():
    while True:
        check_weather()

        choice = input("\nCheck another city? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()

