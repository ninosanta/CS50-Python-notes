# Testin my twttr

In a file called `twttr.py`, reimplement [Setting up my twttr](../../../Lecture%2002%20-%20Loops/Assignments/03_twttr/README.md) from [Assignments of Lecture 02](../../../Lecture%2002%20-%20Loops/Assignments/../../Lecture%2005%20-%20Unit%20Tests/Assignments/01_testing_my_twttr/README.md), restructuring your code per the below, wherein `shorten` expects a `str` as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
```python
def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called `test_twttr.py`, implement **one or more** functions that collectively test your implementation of `shorten` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:
```bash
$ python3 -m pytest
```