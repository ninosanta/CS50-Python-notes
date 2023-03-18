import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.fullmatch(r"(\d\d?\d?)\.(\d\d?\d?)\.(\d\d?\d?)\.(\d\d?\d?)", ip):
        try:
            if len(matches.groups()) == 4 and all(
                0 <= int(n) <= 255 for n in matches.groups()
            ):
                return True
            else:
                return False
        except ValueError:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
