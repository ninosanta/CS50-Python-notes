# Debugging


def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(height):
    for i in range(height):
        # print(i, end=" ")
        print("#" * (i + 1))


if __name__ == "__main__":
    main()
