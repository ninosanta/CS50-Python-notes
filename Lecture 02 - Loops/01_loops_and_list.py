def cat():
    n = int(input("How many cats do you have? "))

    while n > 0:
        print("Meow")
        n -= 1


# List
def cat_list():
    n = int(input("How many cats do you have? "))

    for _ in [0, ..., n]:  # range(n) is equivalent
        print("Meow")


# Pythonically
def cat_pythonic():
    n = int(input("How many cats do you have? "))

    print("Meow\n" * n, end="")


# Correct input
def cat_correct():
    while True:
        n = int(input("How many cats do you have? "))
        if n > 0:
            break

    for _ in range(n):
        print("Meow")


def get_number():
    while True:
        n = int(input("What's n? "))
        if n >= 0:
            return n


def meow():
    for _ in range(get_number()):
        print("meow")


# list length -> len
def hogwarts():
    students = ["Hermonie", "Harry", "Ron", "Draco", "Luna", "Neville"]

    for student in students:
        print(student)

    """len"""
    for i in range(len(students)):
        print(i + 1, students[i])


hogwarts()
