import requests     # "pip install requests" or "pip3 install requests"

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            print("❌ Failed to fetch joke.")
            return

        data = response.json()
        print(data)
        setup = data.get("setup")
        punchline = data.get("punchline")

        print("\n😂 Random Joke")
        print(setup)
        input("Press Enter for punchline...")
        print(punchline)

    except requests.exceptions.RequestException:
        print("❌ Network error. Please try again.")

def main():
    while True:
        get_random_joke()

        choice = input("\nGet another joke? (y/n): ").lower()
        if choice != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()
