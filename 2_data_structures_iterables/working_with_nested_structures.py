# e-learning code - working with nested data structures
#
# employees = [
#     {"name": "John","age": 35,"position": "Manager", "department": "Sales"},
#     {"name": "Ana","age": 28,"position": "Engineer", "department": "IT"},
#     {"name": "Carlos", "age": 42, "position": "Director",
#         "department": "Operations"}
# ]
#
# for emp in employees:
#    # print (f'{emp["name"]} is in the {emp["department"]} department.')
#     print(f'{emp["name"]} is a {emp["position"]} working in the {emp["department"]} department.')


students = [
    {'name': 'Alice', 'age': 20, 'grades': [90, 85, 95]},
    {'name': 'Bob', 'age': 21, 'grades': [80, 75, 70]},
    {'name': 'Charlie', 'age': 19, 'grades': [95, 90, 92]},
]

for student in students:
    # grades holds the grades list for the loops current iteration
    grades = student['grades']

    # sum of grades divided by length of list is an average calculation
    avg_grade = sum(grades) / len(grades)

    # creates a new key-value for each student
    student['avg_grade'] = round(avg_grade,2)

print (students)