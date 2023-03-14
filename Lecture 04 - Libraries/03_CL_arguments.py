# Command-line Arguments
import sys


def name():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")

    print(
        "Hello, my name is", sys.argv[1].capitalize()
    )  # sys.argv[0] is the name of the script, then
    # there are the actual passed arguments.


def names():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")

    # Slice of `argv`
    for name in sys.argv[
        1:
    ]:  # sys.argv[1:] bypasses the first element, i.e., the name of the script
        print("Hello, my name is", name.capitalize())


def main():
    # name()
    names()


if __name__ == "__main__":
    main()
