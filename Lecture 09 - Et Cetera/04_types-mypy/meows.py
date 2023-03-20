# It turns ou that Python does require the explicit declaration of types.
# Nevertheless, it’s good practice need to ensure all of your variables 
# are of the right type.
# `mypy` is a program that can help you test to make sure all your variables
# are of the right type.
# You can install `mypy` by executing in your terminal window: 
#   `pip install mypy`
#
# Python accepts type hints, which are a way to tell the interpreter what
# type a variable is. This is not required, but it is good practice.
# Type hints are not enforced by the interpreter, but they can be checked
# by mypy.

def meow(n: int) -> None:  # two type hints
    for _ in range(3):
        print("meow")

number: int = input("Nymber: ")  # type hint
meow(number)
# running mypy meows.py will give you an error:
#   meows.py:18: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
#   Found 1 error in 1 file (checked 1 source file)