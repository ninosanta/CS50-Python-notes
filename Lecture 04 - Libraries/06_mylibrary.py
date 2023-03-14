# It is possibile to import a module from a different directory.
import sys
from mylibrary import sayings
from mylibrary.sayings import goodbye


def main():
    if len(sys.argv) == 2:
        sayings.hello(sys.argv[1])
        goodbye(sys.argv[1])


if __name__ == "__main__":
    main()
