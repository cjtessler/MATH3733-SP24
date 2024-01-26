# Project: Guessing

from utils import validated_input, get_random_positive_int, print_banner
from time import sleep

ROBOT = "\U0001F916"
MONKEY_CLOSED_EYES = "\U0001F648"
HUMAN = "\U0001F468"

SLEEP_TIME = 1

##########################################################
#################### Student Code ########################
##########################################################


# Part 1
def play_guess_mode():
    # TODO
    print("Implement play_guess_mode then delete this print statement\n")


# Part 2
def play_generator_mode_easy():
    # TODO
    print("Implement play_generator_mode_easy then delete this print statement\n")


# Part 3
def play_generator_mode_medium():
    # TODO
    print("Implement play_generator_mode_medium then delete this print statement\n")


# Part 4
def play_generator_mode_hard():
    # TODO
    print("Implement play_generator_mode_hard then delete this print statement\n")


# Part 5
# Write any utility function you need here.
# The grader will use the default implementation of utils.py.


##########################################################
#################### Starter Code ########################
##########################################################


def human_responds(guess, target) -> int:
    """
    Compares the guess and target and prints an appropriate to the standard output.

    Returns -1 if the guess is too low.
    Returns 1 if the guess is too high.
    Returns 0 if the guess is the target (otherwise).
    """
    if guess < target:
        print(f"{HUMAN}: Too low!")
        return -1
    elif guess > target:
        print(f"{HUMAN}: Too High!")
        return 1
    else:
        print(f"{HUMAN}: That's it!")
        return 0


def select_game_mode():
    """Prompts the user to select game mode."""
    print("How do you want to play?")
    print("1: as the guesser")
    print("2: as the number generator")
    mode = 3
    while mode > 2:
        mode = validated_input("> ")

    return mode


def play_game() -> int:
    """Prompts the user to setup the game."""
    # Select game mode
    mode = select_game_mode()
    play_again = False

    # Select game mode
    if mode == 1:
        play_guess_mode()
    elif mode == 2:
        select_generator_mode()

    # Check if user wants to play again
    play_again = replay()

    return play_again


def select_generator_mode():
    """Prompts the user to select a difficulty."""
    print("Hello Human! Select a difficulty.")
    print("1: Easy")
    print("2: Medium")
    print("3: Hard")

    difficulty = validated_input("> ")
    if difficulty == 1:
        print("Easy mode selected!")
        play_generator_mode_easy()
    elif difficulty == 2:
        print("Medium mode selected!")
        play_generator_mode_medium()
    elif difficulty == 3:
        print("Hard mode selected")
        play_generator_mode_hard()
    else:
        print("That was not an option...")
        sleep(SLEEP_TIME)
        print("Since you are being difficult...")
        sleep(SLEEP_TIME)
        print("Hard mode selected")
        play_generator_mode_hard()


def replay() -> bool:
    """Prompts the user if they would like to replay."""
    print("Play again?")
    print("1: Yes")
    print("2: No")

    response = float("inf")
    while response > 2:
        response = validated_input("> ")

    if response == 1:
        return True
    else:
        return False


def main():
    """The main entry point to the game."""
    # Print banner
    print_banner()

    # Initialize variable for game loop
    play_again = True

    # Game loop
    while play_again:
        play_again = play_game()

    # Print salutation
    print("Thanks for playing!")


# TO learn about __name__ == "__main__" see
# https://youtu.be/sugvnHA7ElY
if __name__ == "__main__":
    main()
    
    # To test specific functions, you might want to comment out the main() call
    # and uncomment the function call you want to test.
    # play_guess_mode()
    # play_generator_mode_easy()
    # play_generator_mode_medium()
    # play_generator_mode_hard()


