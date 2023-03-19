# Put everything related to the Student inside the class

class Student:
    def __init__(self, name=None, house=None):
        self.name = name  # will call the setter
        self.house = house  # idem

    def __str__(self):
        return f"{self.name} is in {self.house}"

    @classmethod    
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()  # student object is created by the class method
    print(student)


if __name__ == "__main__":
    main()
