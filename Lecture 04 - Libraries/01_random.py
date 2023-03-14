# The `import` keyword in Python is used to import the contents/functions
# from modules that someone's written.
""" Whole module import: """
import random

# The `from` keyword, instead, is used to import specific functions from a module.
from random import choice  # this allows to call `choice()` directly instead of

# `random.choice()`. However, this may lead name clashes
# because it is not specified that the choice() function
# is the one of the `random` module.


def flip_coin():
    # random.choice(seq) where `seq` is a sequence (list, tuple, string)
    return random.choice(["heads", "tails"])


def randint(a, b):
    # random.randint(a, b) returns a random integer N such that a <= N <= b
    # where each number has the same probability of being chosen.
    return random.randint(
        a, b
    )  # lol, the function uses the same name as the one of the module


def shuffle(lst):
    # random.shuffle(lst) shuffles the list `lst` **in place**
    random.shuffle(lst)


def main():
    print(flip_coin())
    print(randint(1, 10))
    cards = ["jack", "queen", "king", "ace"]
    shuffle(cards)
    print(cards)  # the cards were shuffled in place


if __name__ == "__main__":
    main()
