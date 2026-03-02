def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
        return False

def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
        return False

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
        return False

def has_symbol(password):
    symbols = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"
    for char in password:
        if char.isupper():
            if char in symbols:
                return True
        return False


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:          # score + 1 or feedback
        pass
    if has_uppercase(password):
        pass
    if has_lowercase(password):
        pass
    if has_digit(password):
        pass
    if has_symbol(password):
        pass

    return score, feedback

def main():
    print("=== Password Strength Checker ===")
    
    while True:
        password = input("\nEnter your password: ")
        score, feedback = check_password_strength(password)

        print("\nPassword Strength Result:")
        if score <= 2:
            print("❌ Weak")
        elif score <= 4:
            print("⚠️ Medium")
        else:
            print("✅ Strong")

        print("\nSuggestions to improve your password:")
        # feedback

        choice = input("\nCheck another password? (y/n): ").lower()
        if choice != "y":
            print("\nGoodbye! 👋")
            break

if __name__ == "__main__":
    main()

