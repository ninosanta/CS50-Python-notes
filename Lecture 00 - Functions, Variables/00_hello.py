# Ask user for their name
name = input("Hello, friend. What is your name? ")  # input gets a string from stdio
# and stores it in a variable
# Say hello to the user
print("hello, " + name)
print("hello,", name)  # multiple arguments to print lead to automatic space addition


""" Named Parameters """
# in official python documentation we find:
#       print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# so it may receive many parameters and some of them are optional and
# others are the so-called named parameters.
# Those named parameters have a default value e.g., the end default value is
# the '\n' so that the print function adds everytime the '\n' at its end!
print("hello, ", end="")  # no new line!
print(name)
print("hello,", name, sep="_")

# quotes in print
print('hello, "friend" or...', 'hello, "friend"')

# Special string: format String or f-String
print(f"hello, {name}")  # watchout for the f before the string!


#############################################################
#                       String Methods                      #
#############################################################
name = "     pippo   johnny   "

name = name.strip()  # remove whitespaces from str
name = name.capitalize()  # capitalize user's name
print(f"hello, {name}")
name = name.title()  # title book capitalization
print(f"hello, {name}")

# function chaining
name = input("What is your name bro?\n").strip().title()
print(f"Hello, {name}")

# Splitting strings:
#   split user's name into first and last name
first_name, last_name = name.split(" ")
print(f"Hello, {first_name}")
