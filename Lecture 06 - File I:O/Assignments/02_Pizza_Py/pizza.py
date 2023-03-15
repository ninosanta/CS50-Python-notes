from tabulate import tabulate
import sys
from os.path import isfile
import csv


def read_table(filename):
    table = []
    with open(filename) as fp:
        reader = csv.reader(fp, delimiter=",")
        for row in reader:
            table += [row]
    return table


def print_table(table):
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))


def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: python {sys.argv[0]} <filename>.csv")
    elif not isfile(sys.argv[1]):
        sys.exit(f"File {sys.argv[1]} does not exist")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit(f"{sys.argv[1]} must be a .csv file")

    print_table(read_table(sys.argv[1]))


if __name__ == "__main__":
    main()
