# We can define a function as a `generator` such that it can be used
# to generate a massive amount of data returning them a little bit 
# at a time instead of all at once. This is useful when we want to
# process a large amount of data without having to store it all in
# memory at once and without running out of memory/CPU.
#
# The keyword `yield` is used to return a value from a generator

def main():
    n = int(input("Number: "))
    print(*sheep(n), sep="\n", end="")


# def sheep(n):  # breaks the computer with large n, e.g., 1000000
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * (i + 1))
#     return flock


def sheep(n):
    for i in range(n):
        yield "🐑" * (i + 1)  # `yeald` returns an iterator


if __name__ == "__main__":
    main()
