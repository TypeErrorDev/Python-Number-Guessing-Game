"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
from random import randint
from statistics import mean, median, mode


# Create the start_game function.
def start_game():
    # Display an intro/welcome message to the player.
    def intro():
        print(
            """
            Lets play a game. If you guess my number that is between 1-100, you'll win the game.
            Guess wrong, and....yup you guessed it...you'll lose the game.
            """)

    intro()

    guesses = []
    high_score = []
    solution = randint(1, 100)
    # For testing purposes, I'm printing the solution to the console.
    print(f"The solution is: {solution}")

    # statistics function
    def game_stats():
        guess_mean = mean(guesses)
        guess_median = median(guesses)
        guess_mode = mode(guesses)
        high_score.append(len(guesses))
        print(f"    Here's your high score: {min(high_score)}")
        print(f"    Total Guesses: {len(guesses)}")
        print(f"    Mean of your Guess: {int(guess_mean)}")
        print(f"    Median of your Guesses: {int(guess_median)}")
        print(f"    Mode of your Guesses: {int(guess_mode)}")

    def add_to_list(item):
        guesses.append(item)
        guesses.sort()

    def play_again():
        while True:
            another_turn = input("Let's play again? Y/N: ")
            if another_turn.lower() == "y":
                print(f"Here is your current High Score: {min(high_score)}\nLet's see if you can beat it!")
                start_game()
                break
            elif another_turn.lower() == "n":
                print("OK. Maybe next time!")
                return
            else:
                print("Please enter 'Y' or 'N'.")

    while True:
        try:
            guess = int(input("So, what's your guess: "))
        except ValueError:
            print("Sorry, please only input integers.")
        else:
            if guess > 100 or guess < 1:
                print("Sorry, please keep the guesses between 1-100 ")
                continue
            elif guess > solution:
                add_to_list(guess)
                print("It's Lower")
                continue
            elif guess < solution:
                add_to_list(guess)
                print("It's Higher")
                continue
            elif guess == solution:
                add_to_list(guess)
                print(
                    "You have survived the night...This time. \nHere's some stats from the night:")
                game_stats()
                play_again()
                break


start_game()
