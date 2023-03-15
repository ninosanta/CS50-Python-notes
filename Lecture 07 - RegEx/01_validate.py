# In Python there is a library called "re" which is used
# to work with Regular Expressions.
# A RE is a pattern, ad this library is used to check if
# a string contains the specified search pattern,
# to validate inputs, to replace parts of a string, to
# split a string into substrings, etc.
#
# One of the most important module in the re library is
# the re.search(pattern, string, flags=0) function,
# which takes a regular expression pattern and a string
# and searches for that pattern within the string.
#
# A pattern can contain special characters:
#   . any character except a newline
#   * 0 or more repetitions
#   + 1 or more repetitions
#   ? 0 or 1 repetition -> optional
#   {m} m repetitions
#   {m,n} range m–n repetitions
#   ^ matches the start of the string
#   $ matches the end of the string or just before the
#     newline at the end of the string
#   [] set of specific characters allowed
#   [^] complementing the set, i.e., elements that must not be in the pattern
#   \d decimal digit
#   \D not a decimal digit
#   \s whitespace characters
#   \S not a whitespace character
#   \w word character... as well as numbers and the underscore
#   \W not a word character
#   A|B either A or B
#   (...) a group
#   (?:...) non-capturing version


import re


def simple_check(email):
    # at least one character, followed by an @, followed by
    # at least one character, followed by a dot, followed by
    # at least one character
    if re.search(
        r".+@.+\..+", email
    ):  # r means raw string: to avoid Python misinterpreting the escape inside the pattern
        return True
    else:
        return False
    # doesn't work for email addresses like "trolol foo@@@bar.com."


def simple_check1(email):
    # constrain the start and end of the string:
    # in this way the email must be one word with no spaces and end with .edu
    # but also no '@' before and after the actual '@' is allowed
    if re.search(r"^[^@]+@[^@]+\.edu$", email):
        return True
    else:
        return False
    # .edu@something.edu still passes


def final_check_long(email):
    if re.search(r"^[a-zA-Z0-9._]+@[a-zA-Z0-9.]+\.edu$", email):
        return True
    else:
        return False
    # toooo long.


def final_check_almost(email):
    # recurring patterns have been simplified in aliases
    if re.search(r"^[\w.]+@[\w.]+\.(com|it|org|edu)$", email):
        return True
    else:
        return False
    # this will fail if the email will be all in uppercase, domain included


def final_check_maybe(email):
    # we can use the flag re.IGNORECASE or use email.lower()...
    if re.search(r"^[\w.]+@[\w.]+\.(com|it|org|edu)$", email, re.IGNORECASE):
        return True
    else:
        return False
    # the problem here though is that ......@.....edu (or with underscores) will pass


# Stop it! Here's the final solution... good luck:
def final_check(email):
    if re.search(
        r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
        email,
        re.IGNORECASE,
    ):
        return True
    else:
        return False
    # moral: just find and use a library to perform email validations


def main():
    email = input("What's your email address? ").strip()

    if final_check(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()


# notes:
#   - re.match(pattern, string, flags=0) -> match only at the beginning of the string,
#     i.e., without specifying the ^ at the beginning of the pattern
#   - re.fullmatch(pattern, string, flags=0) -> match the whole string, i.e., without
#     specifying the ^ at the beginning and the $ at the end of the pattern
