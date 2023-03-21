def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# $##.## format
def dollars_to_float(d):
    #return float(d.replace("$", ""))
    return float(d[1:])  # from the second character to the end


# ##% format
def percent_to_float(p):
    #return float(p.replace("%", "")) / 100
    return float(p[:-1]) / 100  # from the beginning to the second to last character


if __name__ == "__main__":
    main()