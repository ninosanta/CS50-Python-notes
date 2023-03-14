import random


def get_number(prompt):
    while True:
        try:
            match int(input(prompt)):
                case n if n <= 0:
                    raise ValueError
                case _:
                    return n
        except ValueError:
            print("That is not a positive integer! Please, try again.")


def main():
    level = get_number("Level: ")
    sol = random.randint(1, level)

    while True:
        guess = get_number("Guess: ")
        if guess < sol:
            print("Too small!")
        elif guess > sol:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
