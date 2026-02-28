import time
import random

def progress_bar(value, max_value, width = 20):
    filled = int((value / max_value) * width)
    return "[" + "#" * filled + "-" * (width - filled) +"]"

def quiz_mode(number):
    print("\n---QUIZ MODE---\n")
    score = 0
    questions = random.sample(range(1,11),5)

    for i, multiplier in enumerate(questions, 1):
        answer = number * multiplier
        print(f"Q{i}/5: {number} x {multiplier} = ?")
        try:
            guess = int(input("Your answer :"))
            if guess == answer:
                print("CORRECT!\n")
                score +=1
            else:
                print(f"WRONG! The answer was {answer}\n")
        
        except ValueError:
            print(f"Invalid input! The answer was {answer}\n")

    print(f"Quiz Score : {score}/5{' --PERFECT!' if score == 5 else ''}")

def run():
    print("=" * 45)
    print("       MULTIPLICATION EXPLORER")
    print("=" * 45)

    try:
        number = int(input("\nEnter a number: "))
    except ValueError:
        print("Invalid Input!. Exiting.")
        return
    
    table   ={i: number * i for i in range(1,11)}
    max_result = max(table.values())

    print(f"\n Multiplication Table for {number}\n")
    print(f" {'#' * 4}{'Expression':<14} {'Result':<8} {'Scale'}")
    print(f"{'-'*4}{'-'*14}{'-'*8}{'-'*22}")

    for i , result in table.items():
        bar = progress_bar(result, max_result)
        line = f" {i:<4} {number} x {i:<10} {result:<8} {bar}"
        print(line)
        time.sleep(0.1)

    print(f"\n{'-'*45}")
    print(f"   Stats for {number}:")
    print(f"    Largest result : {max_result}")
    print(f"    Sum of all : {sum(table.values())}")
    print(f"    Even results : {sum(1 for v in table.values() if v%2 == 0)}/10")
    print(f"    Odd results : {sum(1 for v in table.values() if v%2 != 0)}/10")
    if all(v % 5 == 0 for v in table.values()):
        print(f"     All are divisible by 5!")
    if all(v % 10 == 0 for v in table.values()):
        print(f"     All are divisible by 10!")

    print(f"{'-'*45}")

    if input("\nTake a quick quiz? (y/n):").lower() == "y":
        quiz_mode(number)

    print("\nThanks for Exploring!!!")

run()


