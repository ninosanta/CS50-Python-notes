import sys
import inflect
from datetime import date


def seasons(input):
    p = inflect.engine()
    try:
        yyyy, mm, dd = input.split("-")
        yyyy = int(yyyy)
        mm = int(mm)
        dd = int(dd)
        birthdate = date(yyyy, mm, dd)
    except ValueError:
        sys.exit("Invalid date")

    minutes = (
        date.today() - birthdate  # timedelta object
    ).total_seconds()  / 60

    return(f"{p.number_to_words(int(minutes), andword='').capitalize()} minutes")
    

def main():
    birth = input("Date of birth (YYYY-MM-DD): ")
    print(seasons(birth))

if __name__ == "__main__":
    main()