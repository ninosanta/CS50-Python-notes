def number():
    try:  # to try something that can cause an error
        x = int(input("Enter a number: "))
    except ValueError:  # if the error is a ValueError
        print("Please, enter an integer")
    else:
        print(f"x is {x}")


def get_number():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            print("Please, enter an integer")
        else:
            return x  # better than `break` and then return x outside the loop


def get_number_shorter():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Please, enter an integer")


# `pass` the exception further
def get_number_pass():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass


def get_int(prompt="Please, enter an integer: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


main()
