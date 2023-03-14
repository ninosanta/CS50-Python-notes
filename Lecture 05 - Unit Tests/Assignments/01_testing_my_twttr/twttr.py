def main():
    str = input("Input: ")
    print(f"Output: {shorten(str)}")


def shorten(word):
    str = ""
    for c in word:
        match c:
            case "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
                continue
            case _:
                str += c
    return str


if __name__ == "__main__":
    main()
