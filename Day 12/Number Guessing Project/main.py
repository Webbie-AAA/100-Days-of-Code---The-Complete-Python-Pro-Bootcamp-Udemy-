import random

def game():
    global guesses
    while guesses != 0:
        print(f"You have {guesses} attempts to guess the number")
        user_guess = int(input("\nGuess a number between 1 and 100:\t"))
        if user_guess == CHOSEN_NUMBER:
            print(f"You win! The number was {CHOSEN_NUMBER}")
            break
        elif user_guess > CHOSEN_NUMBER:
            print("Too high. Guess again")
            guesses -= 1
        elif user_guess < CHOSEN_NUMBER:
            print("Too low. Guess again")
            guesses -= 1
    if guesses == 0:
        print(f"You've run out of guesses. The number was {CHOSEN_NUMBER}")


game_play = True
while game_play:
    CHOSEN_NUMBER = random.randint(1, 100)
    level = input("\nChoose a difficulty. Type 'easy' or 'hard':\t").lower().strip()

    if level == "easy":
        guesses = 10
        game()

    elif level == "hard":
        guesses = 5
        game()





