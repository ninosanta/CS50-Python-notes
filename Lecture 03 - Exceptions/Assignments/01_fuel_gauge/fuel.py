import sys


def main():
    print(gauge(convert()))


def convert():
    while True:
        fraction = input("Enter a fraction: ")
        try:
            f = fraction.split("/")
            x = int(f[0])
            y = int(f[1])
            if x > y:
                raise ValueError
            if y == 0:
                raise ZeroDivisionError
            break
        except (IndexError, ValueError, ZeroDivisionError):
            print("Invalid fraction. Please, try again")
            continue
    return round((x * 100 / y))


def gauge(percentage):
    return "E" if percentage <= 1 else "F" if percentage >= 99 else f"{percentage}%"


if __name__ == "__main__":
    main()
