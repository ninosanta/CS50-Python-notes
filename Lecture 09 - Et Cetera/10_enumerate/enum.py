# `enumerate` that iterates on a sequence and returns a tuple 
# of the index and the value at that index

students = ["Harry", "Ron", "Hermione"]

for i, student in enumerate(sorted(students)):
    print(f"Student {i + 1}: {student}")

