# Tuples in Python are collection of values that, differentely from lists, are
# immutable but can be accessed by index as lists
def get_student_tuple():
    name = input("Name: ")
    house = input("House: ")

    return (name, house)  # parenthesis are optional


def get_student_list():
    name = input("Name: ")
    house = input("House: ")

    return [name, house]  # mutable


# dictionaries are better because have a well defined semantycs
# for values
def get_student_dict():
    name = input("Name: ")
    house = input("House: ")

    return {
        "name": name,
        "house": house,
    }


def main():
    student = get_student_dict()  # immutable
    # print(f"{student[0]} is in {student[1]}")
    print(f"{student['name']} is in {student['house']}")


if __name__ == "__main__":
    main()
