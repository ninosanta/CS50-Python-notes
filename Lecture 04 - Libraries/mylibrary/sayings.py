def hello(name="No name provided"):
    print(f"Hello, {name.capitalize()}!")


def goodbye(name="No name provided"):
    print(f"Goodbye, {name.capitalize()}!")


def main():
    hello("Alice")
    hello("Bob")
    goodbye("Alice")
    goodbye("Bob")


# __name__ is a special variable in Python whose value is set from Python
# to __main__ when a file is ran from command line.
# If a file is imported from another file, __name__ of the imprted file
# will be set to the name of the module.
# This allows to not run the code in the if __name__ != "__main__" as it will
# be when this library will be imported to another file, i.e., in that case
# the "__name__" == "__main__" will be the one inside the "importer"
if __name__ == "__main__":
    main()
