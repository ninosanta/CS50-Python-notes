import sys


def main():
    print(gauge(convert(input("Enter a fraction: "))))


def convert(fraction):
    try:
        f = fraction.split("/")
        x = int(f[0])
        y = int(f[1])
        if x > y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
    except (IndexError, ValueError, ZeroDivisionError):
        return sys.exit("Invalid fraction")
    return round((x * 100 / y))


def gauge(percentage):
    return "E" if percentage <= 1 else "F" if percentage >= 99 else f"{percentage}%"


if __name__ == "__main__":
    main()
