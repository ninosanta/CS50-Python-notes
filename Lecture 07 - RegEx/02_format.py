# Format the input in the way you want

import re


def format(name):
    re.search


def main():
    names = [
        "David Malan",
        "Malan, David",
        "Malan,        David",
        "Malan, David, Jr.",
        "Malan, David, Sr.",
        "Malan,David",
    ]

    for name in names:
        print(f"{name} {format2(name)}")


def format1(name):
    # searches also returs as a match object what specified as
    # a group in the regex, i.e., between the parentheses
    matches = re.search(r"^(.+), *(.+)$", name)
    if matches:
        # last, first = matches.groups() is possible
        # But also acces to a single group, e.g., matches.group(0) is the whole match
        return f"becomes {matches.group(2)} {matches.group(1)}"
    else:
        return f"remains {name}"


# Walrus operator := is a new assignment operator in Python 3.8.
# It assigns the value of the expression on the right to the variable on the left
# and returns the value of the expression
def format2(name):
    # Walrus operator
    if matches := re.search(r"^([^,]+), *([^,]+),? *(.*)$", name):
        return f"becomes {matches.group(2)} {matches.group(1)} {matches.group(3)}"
    else:
        return f"remains {name}"


if __name__ == "__main__":
    main()
