# Inheritance is, perhaps, the most powerful feature of object-oriented
# programming.
# It just so happens that you can create a class that “inherits” methods,
# variables, and attributes from another class.


class Wizard:
    def __init__(self, name=None):
        if not name:
            raise ValueError("Missing name")
        self.name = name


# In parantheses, we specify the class from which we want to inherit.
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)  # call the parent's constructor
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


def main():
    wizard = Wizard("Gandalf")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Snape", "Potions")

    print("Wizard", wizard.name)
    print("Student", student.name,"in", student.house)
    print("Professor", professor.name,"teaches", professor.subject)


if __name__ == "__main__":
    main()
