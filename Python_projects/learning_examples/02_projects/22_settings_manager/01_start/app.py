import json
from pathlib import Path

SETTINGS_FILE = Path("settings.json")
DEFAULT_SETTINGS = {
    "username": "guest",
    "theme": "light",          # light / dark
    "volume": 50,              # 0 - 100
    "notifications": True      # True / False
}

def load_settings():
    pass
def save_settings(settings):
    pass
def show_settings(settings):
    pass
def set_setting(settings):
    pass
def reset_settings():
    pass

def main():
    settings = load_settings()

    while True:
        print("\n=== Settings Manager ===")
        print("1) View settings")
        print("2) Change a setting")
        print("3) Reset to defaults")
        print("4) Exit")

        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            show_settings(settings)
        elif choice == "2":
            set_setting(settings)
        elif choice == "3":
            settings = reset_settings()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("❌ Please choose 1-4.")

if __name__ == "__main__":
    main()

