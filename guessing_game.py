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
        print("Lets play a game. If you guess my number that is between 1-100, you'll win the game.\nGuess wrong, and....yup you guessed it...you'll lose the game.")
    intro()

    guesses = []
    # TODO Need to display a high score, or a "No High Score"
    high_score = []
    solution = randint(1, 100)
    print(f"The solution is: {solution}")

    # statistics function
    # TODO: Need to change the mean/median/mode to the `tries` list, and not the guesses list
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
            play_again = input("Let's play again? Y/N: ")
            if play_again.lower() == "y":
                print(f"Here is your current High Score: {min(high_score)}\nLet's see if you can beat it!")
                break
            elif play_again.lower() == "n":
                print("OK. Bye!")
                return
            else:
                print("Please enter 'Y' or 'N'.")  
                 

    # Continuously prompt the player for a guess.
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
                



    # TODO Need to complete the below
    #   6. Prompt the player to play again
    #     a. If they decide to play again, start the game loop over.
    #     b. If they decide to quit, show them a goodbye message.
    # TODO Need to reroll new random number


    # TODO Need to save the game_stats to it's own list
start_game()
