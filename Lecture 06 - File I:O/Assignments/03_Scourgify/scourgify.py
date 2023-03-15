import sys
import csv
from os.path import isfile


def main():
    if len(sys.argv) != 3:
        sys.exit(f"Usage: python {sys.argv[0]} <infile> <outfile>")
    elif not isfile(sys.argv[1]):
        sys.exit(f"Error: {sys.argv[1]} does not exist")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Error: both files must be .csv files")

    new_data_format(split_names(sys.argv[1]), sys.argv[2])


def split_names(infile):
    data = []
    with open(infile) as fp:
        reader = csv.DictReader(fp)  # no fieldnames= required!!
        for dict in reader:
            last, first = dict["name"].strip().split(",")
            data += [{"first": first, "last": last, "house": dict["house"]}]
    return data


def new_data_format(data, outfile="after.csv"):
    with open(outfile, "w") as fp:
        writer = csv.DictWriter(fp, fieldnames=["first", "last", "house"])
        writer.writeheader()  # do not forget it!
        for dict in data:
            writer.writerow(dict)


if __name__ == "__main__":
    main()
