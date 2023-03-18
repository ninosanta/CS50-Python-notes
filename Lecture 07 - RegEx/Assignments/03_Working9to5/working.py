import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # group 1: from one up to two digits
    # group 2: if there is a colon followed from one up to two digits. Take the digits
    # group 3: AM or PM
    # group 4: from one up to two digits
    # group 5: if there is a colon followed from one up to two digits. Take the digits
    # group 6: AM or PM
    matches = re.search(
        r"(\d{1,2})(?::(\d{1,2})?)? (AM|PM)(?: to) (\d{1,2})(?::(\d{1,2})?)? (AM|PM)", s
    )

    try:
        h1 = int(matches.group(1))
        m1 = int(matches.group(2)) if matches.group(2) else 0
        t1 = matches.group(3)
        h2 = int(matches.group(4))
        m2 = int(matches.group(5)) if matches.group(5) else 0
        t2 = matches.group(6)

        if not 0 <= h1 <= 12 or not 0 <= h2 <= 12:
            raise ValueError
        if m1 != None and not 0 <= m1 <= 59:
            raise ValueError
        if m2 != None and not 0 <= m2 <= 59:
            raise ValueError

    except ValueError:
        sys.exit("Invalid input")

    h1 += 12 if (h1 != 12 and t1 == "PM") else -12 if (h1 == 12 and t1 == "AM") else 0
    h2 += 12 if (h2 != 12 and t2 == "PM") else -12 if (h2 == 12 and t2 == "AM") else 0

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


if __name__ == "__main__":
    main()
