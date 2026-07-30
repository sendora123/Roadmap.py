student = {
    "name": " Peter",
    "age": 18,
    "grade": "A",
    "subjects": ["Math", "English", "Computer"]
}

student["club"] = "Debate Club"
print("Added club:", student)

student["grade"] = "A"
print("Updated grade:", student)

del student["age"]
print("Removed age:", student)

print("Second subject:", student["subjects"][1])

print("Final dictionary:", student)