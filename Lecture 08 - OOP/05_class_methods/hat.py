# Sometimes, we want to add functionality to a class itself, 
# not to instances of that class.
# `@classmethod` is a function that we can use to add functionality to 
# a class as a whole.

# Sorting Hat

import random


# this class is a singleton, meaning that there is only one instance of it.
# We do not need more instances of it! A single sorting hat is enough.
class Hat:
    # class variables are shared by all instances of a class
    houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

    @classmethod
    def sort(cls, name):  # cls is a convention for the class reference
        print(name, "is in", random.choice(cls.houses))


def main():
    # no instances of the singleton class are needed, just call the class method:
    Hat.sort("Harry")


if __name__ == "__main__":
    main()