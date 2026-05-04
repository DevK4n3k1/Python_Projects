import json
from pathlib import Path

SETTINGS_FILE = Path("settings.json")

DEFAULT_SETTINGS = {
    "username": "guest",
    "theme": "light",          # light / dark
    "volume": 50,              # 0 - 100
    "notifications": True      # True / False
}

def load_settings() -> dict:
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Settings file is not a valid object.")
        return {**DEFAULT_SETTINGS, **data}  # merge defaults + saved
    except FileNotFoundError:
        return DEFAULT_SETTINGS.copy()
    except (json.JSONDecodeError, ValueError):
        print("⚠️ Settings file is corrupted. Using default settings.")
        return DEFAULT_SETTINGS.copy()

def save_settings(settings: dict) -> None:
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)

def show_settings(settings: dict) -> None:
    print("\n--- Current Settings ---")
    for k, v in settings.items():
        print(f"{k}: {v}")
    print("------------------------")

def set_setting(settings: dict) -> None:
    key = input("Enter setting name (username/theme/volume/notifications): ").strip()

    if key not in settings:
        print("❌ Unknown setting.")
        return

    new_value = input("Enter new value: ").strip()

    # simple type handling
    try:
        if key == "volume":
            new_value = int(new_value)
            if not (0 <= new_value <= 100):
                raise ValueError("Volume must be 0-100.")
        elif key == "notifications":
            lowered = new_value.lower()
            if lowered in ("true", "yes", "y", "1"):
                new_value = True
            elif lowered in ("false", "no", "n", "0"):
                new_value = False
            else:
                raise ValueError("Enter true/false for notifications.")
        elif key == "theme":
            if new_value not in ("light", "dark"):
                raise ValueError("Theme must be 'light' or 'dark'.")
        # username stays as string
    except ValueError as e:
        print(f"❌ Invalid value: {e}")
        return

    settings[key] = new_value
    save_settings(settings)
    print("✅ Saved!")

def reset_settings() -> dict:
    settings = DEFAULT_SETTINGS.copy()
    save_settings(settings)
    print("✅ Reset to defaults!")
    return settings

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
