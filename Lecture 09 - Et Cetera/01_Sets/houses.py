# A `set` is a data structure that stores unique values, i.e. no duplicates.

def main():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Cedric", "house": "Hufflepuff"},
        {"name": "Cho", "house": "Ravenclaw"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Ginny", "house": "Gryffindor"},
        {"name": "Neville", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Luna", "house": "Ravenclaw"},
        {"name": "Pansy", "house": "Slytherin"},
        {"name": "Seamus", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Dean", "house": "Gryffindor"},
        {"name": "Parvati", "house": "Gryffindor"},
    ]

    houses = set()  # empty set
    for student in students:
        houses.add(student["house"])  # add the new value to the set
    for house in sorted(houses):
        print(house)  # no duplicates, as expected


if __name__ == "__main__":
    main()