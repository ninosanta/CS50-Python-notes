# Classes are a way by which, in object-oriented programming,
# we can create our own type of data and give them names.
# A class is like a mold for a type of data – where we can invent
# our own data type and give them a name.
#
# Classes have Attributes that can be accesses with dot notation.
# Objects are instances of a class.

import sys


class Student:
    # dunder method __init__ initializes the object -> constructor
    # self represents the current object instantiated and default values are allowed.
    # It is also suggested to do validation in here.
    def __init__(self, name=None, house=None, patronus=None):
        if not name:
            raise ValueError("Missing name")
        elif house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    # dunder method __str__ is called when we try to print an object
    def __str__(self) -> str:  # -> str: to specify the return type is not necessary
        return f"{self.name} is in {self.house} and has a {self.charm()} patronus."

    # useful for debugging
    def __repr__(self) -> str:
        return f"Student({self.name}, {self.house}, {self.patronus})"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def get_student_variables():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")

    return student


def get_student_constructor():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")

    try:
        return Student(name, house, patronus)  # constructor call
    except ValueError as e:
        sys.exit(e)


def main():
    student = get_student_constructor()  # object of the class
    # print(f"{student.name} is in {student.house}")  # boring
    print(student)  # calls __str__ dunder method if defined


if __name__ == "__main__":
    main()







