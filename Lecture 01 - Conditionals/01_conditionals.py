def main1():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y:
        print("x is less than y")
    elif x == y:
        print("x and y are equal")
    else:
        print("x is greater than y")


# OR
def main2():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    if x < y or x > y:  # x != y
        print("x is not equal to y")
    else:
        print("x and y are equal")


def grade():
    score = int(input("Score: "))

    if score >= 90 and score <= 100:  # AND
        print("Grade: A")
    elif 80 <= score < 90:  # BETWEEN
        print("Grade: B")
    elif score >= 70:  # simplyfication: not necessary to write >= 70 and <= 79
        print("Grade: C")
    elif score >= 60:  # as above, because the first condition met represents the score
        print("Grade: D")
    else:
        print("Grade: F")


def parody():
    x = int(input("What's x? "))

    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")


# Booleans
def is_even(x):
    if x % 2 == 0:
        return True  # capital T!
    else:
        return False  # capital F!


def is_even_pythonic(x):
    return True if x % 2 == 0 else False  # like as we would say in English


def is_even_best(y):
    return y % 2 == 0  # elegant


def check_even():
    x = int(input("What's x? "))

    if is_even_best(x):
        print("x is even")
    else:
        print("x is odd")


# Match
def house():
    name = input("What's your name? ").capitalize()

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Griffindor")
        case "Draco":
            print("Slytherin")
        case _:  # default
            print("Who?")


house()
