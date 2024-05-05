from random import randint
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freedie"]

students_score = {student:randint(0,100) for student in names}
print(students_score)
# print(students_score.__len__())

# {key:value for (key, value) in dictionary.items() if value > 50}

passed_students = {student:score for (student, score) in students_score.items() if score > 50}
print(passed_students)