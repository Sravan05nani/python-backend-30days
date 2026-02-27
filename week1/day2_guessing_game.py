import random

DIFFICULTIES = {
    "1": (1, 10, 5, "Easy"),
    "2": (1, 100, 8, "Medium"),
    "3": (1, 1000, 15, "Hard"),
}

def get_closeness(diff):
    if diff <= 5:
        return "very close :)"
    if diff <= 20:
        return "close :)"
    if diff <= 50:
        return "half way there!"
    if diff <= 100:
        return "far away :("
    return "not even close!"


def play_game():

    print("Choose Difficulty Level:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-100, 8 attempts)")
    print("3. Hard (1-1000, 15 attempts)")

    while True:
        choice = input("\nEnter choice (1, 2 or 3): ").strip()
        if choice in DIFFICULTIES:
            low, high, max_attempts, label = DIFFICULTIES[choice]
            break
        print("Invalid choice!")

    secret = random.randint(low, high)
    score = 1000
    attempts = 0   

    print(f"\nGuess a number between {low} and {high}")
    print(f"You have {max_attempts} valid attempts\n")

    while attempts < max_attempts:

        print("Attempts remaining:", max_attempts - attempts)

        user_input = input("Your Guess: ").strip()
        if user_input == "":
            print("Empty input! Enter a number.\n")
            continue

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid number!\n")
            continue

        if not (low <= guess <= high):
            print(f"Enter number between {low} and {high}\n")
            continue

        attempts += 1
        if attempts > 1:
            score -= 50

        if guess == secret:
            print(f"\nCorrect! You got it in {attempts} attempt(s)!")
            print(f"Final Score: {score}")
            break

        direction = (
            "Guess lower number than this"
            if guess > secret
            else "Guess higher number than this"
        )

        print(get_closeness(abs(guess - secret)))
        print(direction + "\n")

    else:
        print(f"\nGame Over! The number was {secret}.")
        print("Final Score: 0")

    while True:
        again = input("\nPlay Again? (yes/no): ").lower().strip()
        if again == "yes":
            play_game()
            break
        elif again == "no":
            print("Thanks for playing...")
            break
        else:
            print("Enter yes or no.")


play_game()