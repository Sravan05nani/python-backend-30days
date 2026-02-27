import random

DIFFICULTIES = {
    "1" : (1,10,5, "Easy"),
    "2" : (1,100,8, "Medium"),
    "3" : (1,1000,15, "Hard"),
}
def get_closeness(diff):
    if diff <= 5: return "very close :)"
    if diff <= 20: return "close :)"
    if diff <= 50: return "half way there!"
    if diff <= 100: return "far away :("
    return "not even close!"

def play_game():
    print("Choose Difficulty Level:\n1. Easy(1-10, 5 attempts)\n2. Medium(1-100, 8 attempts)\n3. Hard(1-1000, 15 attempts)")
    low, high, max_attempts, label = DIFFICULTIES.get(input("\nEnter choice (1/2/3):"),DIFFICULTIES["2"])

    secret = random.randint(low,high)
    score = 1000

    print(f"\nGuess a number between {low} and {high}! in ({max_attempts} attempts)\n")
    for attempt in range(1,max_attempts+1):
        print("Attempts remaining: ", max_attempts-attempt+1)

        try:
            guess = int(input("Your Guess: "))
        except ValueError:
            print("Please enter valid number!\n")
            continue
        score -= 50
        if guess == secret:
            print(f"\nCorrect! You got it in {attempt} attempt(s)!!")
            print(f"Final score : {score}")
            break

        if not (low <= guess <= high):
            print(f"Out of range! please enter a number between {low} and {high}\n")
            continue

        direction = "Guess lower number than this" if guess > secret else "Guess higher than this"
        print(f"{get_closeness(abs(guess - secret))}\n {direction}\n")

    else:
        print(f"\n Game Over...! The number was {secret}.\nFinal Score : 0")

    if input("\nPlay Again? (yes/no):").lower() == "yes":
        play_game()
    else:
        print("Thanks for playing...")

play_game()