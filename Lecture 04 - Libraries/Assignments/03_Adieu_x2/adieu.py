import inflect

p = inflect.engine()


def get_name():
    return input("Name: ")


def main():
    names = []
    while True:
        try:
            names += [get_name()]  # appendi using `+` operator and the list conversion
        except EOFError:
            print("  ")  # oterwise it will print `^D` too -.- (macOS)
            print("Adieu, adieu, to " + p.join(names))
            break


if __name__ == "__main__":
    main()
