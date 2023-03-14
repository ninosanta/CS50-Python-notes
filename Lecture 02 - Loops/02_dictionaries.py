# dict -> { key : value }
def hogwarts():
    ### Make a corresponece between students and houses using lists
    students = ["Hermione", "Harry", "Ron", "Draco"]
    houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
    ### does not scale well...
    """ Dictionaris are meant to simplify these cases """
    students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin",
    }

    for student in students:
        # the for just iterates over the keys that will be used to access the values
        # as dict[key] -> value
        print(student, "is in", students[student])


def hogwarts_patronus():
    # list of dictionaries
    students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
        {
            "name": "Draco",
            "house": "Slytherin",
            "patronus": None,
        },  # None like undefined in JS
    ]

    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=" - ")


hogwarts_patronus()
