import random

def guess_number_game():
    print("🤔 Guess Number Game")
    print("I'm thinking of a number between 1 and 100.")

    guess = int(input("Enter your guess: "))
    print(guess)

def main():
    while True:
        guess_number_game()

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()

