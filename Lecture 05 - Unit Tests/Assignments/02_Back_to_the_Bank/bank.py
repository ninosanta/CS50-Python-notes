def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    str = greeting.lower()

    if str.startswith("hello"):
        return 0
    elif str.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
