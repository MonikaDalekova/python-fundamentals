# courses = {}
# while True:
#     data = input()
#     if data == "end":
#         break
#     name_course, student_name = data.split(" : ")
#     if name_course not in courses:
#         courses[name_course] = []
#
#     courses[name_course].append(student_name)
#
# for course_name, students in courses.items():
#     print(f"{course_name}: {len(students)}")
#     for student in students:
#         print(f"-- {student}")

#2
def course_members(command):
    course, name = command.split(" : ")
    if course not in courses:
        courses[course] = []
    courses[course].append(name)


def printed_courses():
    for course_name, number_students in courses.items():
        print(f"{course_name}: {len(number_students)}")
        for names in number_students:
            print(f"-- {names}")


courses = {}
command = input()
while command != 'end':
    course_members(command)
    command = input()
printed_courses()