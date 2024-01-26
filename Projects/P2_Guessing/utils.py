# The following file contains utility functions useful for the project.

from random import randint, seed 

# Change the seed value to generator a different sequence of random numbers.
SEED = 1
seed(SEED)


def validated_input(prompt: str) -> int:
    """
    Wrapper function for input that continually prompts
    the user until a positive integer is inputted.
    """
    # Continually ask until valid input is provided
    while True:
        inp = input(prompt)

        try:
            inp = float(inp)
            if inp.is_integer() and inp > 0:
                inp = int(inp)
                break
        except:
            continue

    return inp


def get_random_positive_int(max_int=1_000_000) -> int:
    """
    Wrapper function for random.randint that returns a 
    random positive integer less than max_int.
    max_int == 1,000,000 by default
    """
    if max_int:
        return randint(1, max_int)


def print_banner():
    """Prints a game banner."""
    print(
        """
    #####################
    ### Guessing Game ###
    #####################
    """
    )