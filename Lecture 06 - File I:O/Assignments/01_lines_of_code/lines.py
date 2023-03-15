import sys
from os.path import isfile


def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: python {sys.argv[0]} <filename>.py")
    elif not isfile(sys.argv[1]):
        # to avoid the handle of FileNotFoundError exception if thrown by the open()
        sys.exit(f"File {sys.argv[1]} does not exist")
    elif not sys.argv[1].endswith(".py"):
        sys.exit(f"{sys.argv[1]} must be a .py file")

    with open(sys.argv[1]) as fp:
        codelines = 0
        for line in fp:
            if line.strip().startswith("#") or line.strip() == "":
                continue
            else:
                codelines += 1
        print(f"File {sys.argv[1]} has {codelines} lines of code")


if __name__ == "__main__":
    main()
