"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
from random import randint
from statistics import mean
from statistics import median


# Create the start_game function.
def start_game():
    # Display an intro/welcome message to the player.
    def intro():
        print("Do you want to play a game? Guess the number between 1-100, and you'll survive the night.")
    intro()
    # Store a random number as the answer/solution.
    guesses = []
    solution = randint(1, 100)
    print("The solution is: {}".format(solution))

    # utility functions
    def add_to_list(item):
        guesses.append(item)

    def list_attempts():
        print(f"    Total Guesses: {len(guesses)}")

    def list_mean():
        guess_mean = mean(guesses)
        print(f"    Average Guess: {guess_mean}")
    #   3. Continuously prompt the player for a guess.
    while True:
        try:
            guess = int(input("What's your guess: "))
        except ValueError:
            print("Sorry, please only input integers.")
        else:
            if guess > solution:
                add_to_list(guess)
                print("It's Lower")
                continue
            elif guess < solution:
                add_to_list(guess)
                print("It's Higher")
                continue
            elif guess > 100 or guess < 1:
                print("Sorry, please keep the guesses between 1-100 ")
            elif guess == solution:
                add_to_list(guess)
                print(
                    "You have survived the night...This time. \nHere's some stats from the night:")
                print(list_attempts())
                print(list_mean())
                break

    #     c. The median of the saved attempts list

    #     d. The mode of the saved attempts list
    #   6. Prompt the player to play again
    #     a. If they decide to play again, start the game loop over.
    #     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
start_game()
