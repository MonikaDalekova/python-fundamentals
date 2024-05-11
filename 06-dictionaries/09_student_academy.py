# pair_of_rows = int(input())
# grades_by_student = {}
# for row in range(pair_of_rows):
#     student_name = input()
#     student_grade = float(input())
#     if student_name not in grades_by_student:
#         grades_by_student[student_name] = []
#     grades_by_student[student_name].append(student_grade)
#
# for student, grades in grades_by_student.items():
#     average_grade = sum(grades) / len(grades)
#     if average_grade >= 4.50:
#         print(f"{student} -> {average_grade:.2f}")

#2
def average_grade(a, b):
    if a not in grades_dict.keys():
        grades_dict[a] = []
    grades_dict[a].append(b)
    return grades_dict


n = int(input())
grades_dict = {}
for pair in range(n):
    name = input()
    grade = float(input())
    grades_dict = average_grade(name, grade)
for name, grades in grades_dict.items():
    av_grade = sum(grades) / len(grades)
    if av_grade >= 4.50:
        print(f"{name} -> {av_grade:.2f}")