def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, " + to + "!"  # f-string even as return value :O


if __name__ == "__main__":
    main()
