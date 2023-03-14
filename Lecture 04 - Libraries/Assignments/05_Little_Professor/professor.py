import random


def get_level():
    while True:
        match int(input("Level: ")):
            case n if n <= 0 or n > 3:
                print("1, 2, or 3 are the valid levels. Try again.")
            case n:
                return n


def generate_integer(ndigits):
    if ndigits <= 0 or ndigits > 3:
        raise ValueError("ndigits must be between 1 and 3")
    range_start = 10 ** (ndigits - 1)
    range_end = (10**ndigits) - 1
    return random.randint(range_start, range_end)


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for j in range(4):
            if j == 3:
                print(f"{x} + {y} = {x + y}")
                break

            try:
                z = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue

            if z == x + y:
                score += 1
                print("Correct!")
                break
            else:
                print("EEE")
                continue

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
