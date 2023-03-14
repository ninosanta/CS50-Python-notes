# Manipuplate CSV files


def students():
    with open("students.csv") as file:
        for line in sorted(file):
            row = line.rstrip().split(",")
            print(f"{row[0]} is in {row[1]}")


def students_unpacking():
    with open("students.csv") as file:
        for line in sorted(file):
            # we know in advance that each line has two elements
            # corresponding to name and house. Hence, we can unpack
            # directly the split() result into two variables
            name, house = line.rstrip().split(",")
            print(f"{name} is in {house}")


# sort by `name` (or `house`) and not by "English string"...
def students_dict():
    students = []  # list of dictionaries
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            # student = {} -> student["name"] = name -> student["house"] = house
            # Faster:
            student = {"name": name, "house": house}
            students.append(student)
    for student in sorted(
        students, key=get_name
    ):  # notice the absence of () and argument
        # the function is passed as a reference
        # and applied to each element of the list
        print(
            f"{student['name']} is in {student['house']}"
        )  # notice the use of single quotes inside the f-string
        # to not disorient Python with the double quotes of the f-string


def get_name(student):
    return student["name"]


# lambda functions are anonymous functions, i.e. functions without a name
def students_dict_lambda():
    students = []
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house}
            students.append(student)
    # print the list of students **sorted by house** in reverse order
    for student in sorted(students, key=lambda stu: stu["house"], reverse=True):
        print(f"{student['name']} is in {student['house']}")


def main():
    students_dict_lambda()


if __name__ == "__main__":
    main()
