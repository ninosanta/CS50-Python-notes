# `open`: https://docs.python.org/3/library/functions.html#open
#         is a function that opens a file and returns the file handle
#         to read from or write to it


def names0():
    file = open("names.txt", "a")  # a -> append
    for _ in range(3):
        file.write(input("What's your name? ") + "\n")
    file.close()

    file = open("names.txt", "r")  # r -> read
    for name in file.readlines():
        print(f"hello, {name.capitalize()}", end="")
    file.close()


# to avoid explicit calls to file.close(), we can use `with` statement
# to create a context manager
def names():
    with open("names.txt", "a") as file:
        for _ in range(3):
            file.write(input("What's your name? ") + "\n")

    with open("names.txt", "r") as file:
        for name in file:  # no need to call readlines()!
            print(
                f"hello, {name.rstrip()}"
            )  # rstrip() removes the trailing newline character
            # more elegant than using end=""


def names_sort():
    names = []
    with open("names.txt") as file:  # to just read, we can omit the mode
        for name in file:
            names.append(name.rstrip())

    for name in sorted(names):
        print(f"hello, {name}")


def names_sort_final():  # reverse order
    with open("names.txt") as file:  # to just read, we can omit the mode
        for name in sorted(file, reverse=True):
            print(f"hello, {name.rstrip()}")


def home_sort_final():  # reverse order
    with open("names.txt") as file:  # to just read, we can omit the mode
        for name in sorted(file, reverse=True):
            print(f"hello, {name.rstrip()}")


def main():
    names_sort_final()


if __name__ == "__main__":
    main()
