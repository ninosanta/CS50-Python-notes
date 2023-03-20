# A standard way of commenting your function’s purpose is to use a docstring. 


# Differently from what I've done in the previous snippets, the docstring is
# meant to go inside the function, not outside it.
# There are a lot of tools that can read the docstrings written in a restructured
# text format and generate documentation for you. For example, Sphinx can generate
# HTML documentation
def meow(n):
    # """Meow n times.""" or, more detailed:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number = int(input("Number: "))
meows = meow(number)
print(meows, end="")