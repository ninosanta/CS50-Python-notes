# Built-in classes in Python

def main():
    print(
        "50 has type: ", type(50), '\n',
        "50.0 has type: ", type(50.0), '\n',
        '"50" has type: ', type("50"), '\n',
        "True has type: ", type(True), '\n',
        "[] has type: ", type([]), '\n',
        "list() has type: ", type(list()), '\n',
        "\{\} has type: ", type({}), '\n',
        "None has type: ", type(None), '\n',
        "main has type: ", type(main), '\n',
        "() has type: ", type(()), '\n',
        "set() has type: ", type(set()), '\n',
        "range(0) has type: ", type(range(0))
    )


if __name__ == "__main__":
    main()