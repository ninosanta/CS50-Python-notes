def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6 or not s[:2].isalpha():
        return False
    elif not s.isalnum():
        return False  # special characters found
    else:
        sub = s[2:]  # otherwise it becomes ugly to slice further next
        for i in range(len(sub)):
            if sub[i].isdigit():
                if sub[i] == "0" or not sub[i:].isdigit():
                    return False
                else:
                    return True
        return True  # is_alpha


if __name__ == "__main__":
    main()
