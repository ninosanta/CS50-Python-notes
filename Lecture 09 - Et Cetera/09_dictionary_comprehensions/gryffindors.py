# With dictionary comprehensions, we can create dictionaries 
# on the fly.

students = ["Harry", "Ron", "Hermione"]

# Create a dictionary where the keys are the students' names
# and the values are their house.
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)

