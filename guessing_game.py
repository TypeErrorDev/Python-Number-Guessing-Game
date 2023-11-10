"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
from random import randint
import statistics


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

    # statistics function
    def game_stats():
        guess_mean = statistics.mean(guesses)
        guess_median = statistics.median(guesses)
        guess_mode = statistics.mode(guesses)
        print(f"    Total Guesses: {len(guesses)}")
        print(f"    Mean of your Guess: {int(guess_mean)}")
        print(f"    Median of your Guesses: {guess_median}")
        print(f"    Mode of your Guesses: {guess_mode}")

    def add_to_list(item):
        guesses.append(item)

    # Continuously prompt the player for a guess.
    while True:
        try:
            guess = int(input("What's your guess: "))
        except ValueError:
            print("Sorry, please only input integers.")
        else:
            if guess > solution:
                add_to_list(guess)
                print("It's Lower")
            elif guess < solution:
                add_to_list(guess)
                print("It's Higher")
            elif guess > 100 or guess < 1:
                print("Sorry, please keep the guesses between 1-100 ")
            elif guess == solution:
                add_to_list(guess)
                print(
                    "You have survived the night...This time. \nHere's some stats from the night:")
                game_stats()
                break

    #   6. Prompt the player to play again
    #     a. If they decide to play again, start the game loop over.
    #     b. If they decide to quit, show them a goodbye message.
start_game()
