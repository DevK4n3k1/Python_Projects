import requests

API_KEY = "YOUR_API_KEY"   # ← put your API key here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def check_weather():
    print("\n🌦 Weather Checker")
    city = input("Enter city name: ").strip()

    if not city:
        print("❌ City name cannot be empty.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        if response.status_code != 200:
            print("❌ Could not fetch weather. Check city name or API key.")
            return

        data = response.json()

        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        print(f"\n📍 City: {city}")
        print(f"🌡 Temperature: {temperature:.1f} °C")
        print(f"☁️ Condition: {condition}")

    except requests.exceptions.RequestException:
        print("❌ Network error. Please try again later.")

def main():
    while True:
        check_weather()

        choice = input("\nCheck another city? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()
