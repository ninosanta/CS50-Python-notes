# `pytest` permits to run tests from different directories
# but a file named __init__.py is required in the directory
# (even empty) in order to tell Python that the folder is
# a package (i.e., a module contained in a foldere).
#
# then, we can just give:
#    $ pytest test
# from the parent directory of test
from hello import hello


def test_default():
    assert hello() == "hello, world!"


def test_argument():
    for name in ["Hermione", "Ron", "Harry"]:
        assert hello(name) == f"hello, {name}!"
