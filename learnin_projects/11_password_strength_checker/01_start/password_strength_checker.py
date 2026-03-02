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
        score += 1
    else:
        feedback.append("Use at least 8 characters")
    
    if has_uppercase(password):
        score += 1
    else:
        feedback.append("Use at least 1 uppercase latter")

    if has_lowercase(password):
        score += 1            
    else:
        feedback.append("Use at least 1 lowercase latter")

    if has_digit(password):
            score += 1
    else:
        feedback.append("Use at least 1 diggit")

    if has_symbol(password):
            score += 1
    else:
        feedback.append("Use at least 1 number")


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

        if feedback:
            print("\nSuggestions to improve your password:")
            for tip in feedback:
                print("-", tip)
        else:
            print("\nGreat job! Your password is strong.")

        choice = input("\nCheck another password? (y/n): ").lower()
        if choice != "y":
            print("\nGoodbye! 👋")
            break

if __name__ == "__main__":
    main()
