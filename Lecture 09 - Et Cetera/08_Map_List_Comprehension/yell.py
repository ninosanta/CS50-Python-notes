def main():
    yell("This", "is", "CS50")
    students = [
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Cho", "house": "Ravenclaw"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Ginny", "house": "Gryffindor"},
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
    ]
    yell_students_lc(*students)

def yell(*words):  # variable number of words
    print(*map(lambda word: word.upper(), words))  # unpack


# list comprehension:
def yell_lc(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


def yell_students_lc(*students):
    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]
    # or:
    gryffindors = [ 
        student["name"] for student in filter(lambda s: s["house"] == "Gryffindor", students)
    ]
    print(*map(lambda s: s.upper(), sorted(gryffindors)))


if __name__ == "__main__":
    main()