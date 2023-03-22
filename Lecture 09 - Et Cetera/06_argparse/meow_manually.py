import sys

def main():
    if len(sys.argv) == 1:
        print("meow")
    elif len(sys.argv) == 3 and sys.argv[1] == "-n":
        try:
            n = int(sys.argv[2])
        except ValueError:
            print("Error: n must be an integer")
            return
        print("meow\n" * n, end="")
    else:
        print(f"Usage: {sys.argv[0]} [-n <number>]")


if __name__ == "__main__":
    main()