def names():
    names = []
    for _ in range(3):
        names += [input("What's your name? ")]  # equivalent to names.append(input())
    
    for name in sorted(names):
        print(f"hello, {name.capitalize()}")


def main():
    names()


if __name__ == '__main__':
    main()
