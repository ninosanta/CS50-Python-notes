# Getters and setters permit to control the access to the attributes of an object.
# Properties are a way to define getters and setters in a more elegant way,
# avoiding programmers to mess up attributes.
#
# `@property` is a decorator that allows to define a method as a property.


class Student:
    def __init__(self, name=None, house=None):
        self.name = name  # will call the setter
        self.house = house  # idem

    def __str__(self):
        return f"{self.name} is in {self.house}"

    # Getter:
    @property
    def name(self):
        return (
            self._name
        )  # the underscore is used to avoid name collision with property name

    # Setter
    #   will be called automatically when there will be a tentative of assignment
    #   to the property `name`, e.g., studend.name = "Harry"
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def get_student_constructor():
    name = input("Name: ")
    house = input("House: ")

    return Student(name, house)


def main():
    student = get_student_constructor()
    # Unfortunately in Python there is no way to define a property as read-only
    # because it is based on the honor system that says:
    #   "Don't change the value of a property that starts with an underscore, because
    #    it is meant to be private and you will break the code of the class"
    student._name = "h4cK1G the class"  # won't be prevented by the setter
    print(student)


if __name__ == "__main__":
    main()
