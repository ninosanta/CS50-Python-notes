# Q: what if the CSV contains corner cases, like commas in the row's columns?
#    For exaple, the CVS specifies the particular column by putting the
#    field between double quotes, e.g., Harry,"Number Four, Privet Drive"
# A: use the `csv` module and its `reader` function will figure out the corner cases
import csv


def students_home():
    students = []
    with open("students_v1.csv") as file:
        reader = csv.reader(
            file
        )  # reader reads the CSV file and identifies corner cases
        for name, home in reader:  # unpacking
            students.append({"name": name, "home": home})

    for student in sorted(students, key=lambda stu: stu["name"], reverse=True):
        print(f"{student['name']} is in {student['home']}")


# read a CVS containing as its first row the column field names
# -> csv.DictReader(file, fieldnames=fieldnames)
def students_home_dict():
    students = []
    with open("students_v2.csv") as file:
        reader = csv.DictReader(
            file
        )  # reads each row of the CSV as dictionaries of columns
        for row in reader:  # unpacking
            #students.append(
            #    {"name": row["name"], "home": row["home"]}
            #)  # here the order doesn't matter and the values will be written in the correct order
            # in fact, we can just do:
            students.append(row)

    for student in sorted(students, key=lambda stu: stu["name"]):
        print(f"{student['name']} is in {student['home']}")


def main():
    students_home_dict()


if __name__ == "__main__":
    main()
