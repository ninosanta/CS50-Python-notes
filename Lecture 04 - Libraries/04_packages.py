# A package is a third party library that can be installed
# and pertmits to access functionality that other people have
# implemented.
# - One of the location where to get packages is PyPI (Python Package Index)
#   website: https://pypi.org/
#
# `pip` is the package manager for Python. It allows to install a package
# by just running a command in the terminal.
#       e.g., `pip install cowsay`
# Then we can import the package in our code and use it.

import cowsay
import sys


def say():
    if len(sys.argv) == 2:
        cowsay.cow("hello, " + sys.argv[1])
        cowsay.trex("hello, " + sys.argv[1])


def main():
    say()


if __name__ == "__main__":
    main()
