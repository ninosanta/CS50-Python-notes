#############################################################
#                       Functions                           #
#############################################################
def main():
    name = input("What is your name? ")
    hello()  # it will use the  default value of `to`
    hello(name)

    x = int(input("What's x? "))
    print(f"{x} squared is {square(x)}")


def square(n):
    return n**2  # same as: return n * n, or pow(n, 2)


def hello(to="World"):
    print(f"Hello, {to}!")


main()  # in this way we can call `hello()` even though it
# is defined after `main()`
