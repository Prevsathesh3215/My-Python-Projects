import random
import pandas


names = {
    "student": ["Sathesh", "Faustina", "Nio", "Man", "Nicholas", "Deena"],
    "scores" : [25, 50, 69, 45, 80, 95]
}
#
# new_dict = {student : random.randint(1, 100) for student in names}
# print(new_dict)
#
# passed_marks = {student: new_dict[student] for student in names if new_dict[student] >= 60}

student_data = pandas.DataFrame(names)

# for (key, value) in student_data.items():
#     print(value)

for (index, row) in student_data.iterrows():
    if row.student == "Deena":
        print(row.scores)