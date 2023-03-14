# Write a CSV initialized with the following columns: name, home, house
# as a header row.

import csv


def students_write_csv():
    name = input("Name: ")
    home = input("Home: ")
    house = input("House: ")

    with open("students_v3.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(
            [name, home, house]
        )  # if necessary, the writer will add double quotes


def students_write_csv_dict():
    name = input("Name: ")
    home = input("Home: ")
    house = input("House: ")

    with open("students_v3.csv", "a") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "home", "house"]
        )  # requires the order in which the columns are when writing
        writer.writerow({"name": name, "home": home, "house": house})


def main():
    students_write_csv_dict()


if __name__ == "__main__":
    main()
