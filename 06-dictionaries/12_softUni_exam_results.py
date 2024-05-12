# user_points_dict = {}
# submissions = {}
# while True:
#     data = input()
#     if data == "exam finished":
#         break
#
#     tokens = data.split("-")
#     if len(tokens) == 3:
#         username, language, points = tokens
#         points = int(points)
#         if username not in user_points_dict.keys():
#             user_points_dict[username] = 0
#         if user_points_dict[username] < points:
#             user_points_dict[username] = points
#         if language not in submissions.keys():
#             submissions[language] = 0
#         submissions[language] += 1
#
#     elif len(tokens) == 2:
#         name = tokens[0]
#         del user_points_dict[name]
# print("Results:")
# for name, points in user_points_dict.items():
#     print(f"{name} | {points}")
# print("Submissions:")
# for language, counts in submissions.items():
#     print(f"{language} - {counts}")

#2
def results_output(username, points, language):
    if username not in results.keys():
        results[username] = 0
    if results[username] < points:
        results[username] = points
    if language not in submissions.keys():
        submissions[language] = 0
    submissions[language] += 1
    return results, submissions


def banned_user(username):
    if username in results.keys():
        del results[username]
        return results


results = {}
submissions = {}

command = input()
while command != "exam finished":
    data = command.split("-")
    if len(data) > 2:
        username, language, points = command.split("-")
        points = int(points)
        results, submissions = results_output(username, points, language)
    else:
        username, action = command.split("-")
        results = banned_user(username)
    command = input()

print("Results:")
for username, points in results.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, submissions_count in submissions.items():
    print(f"{language} - {submissions_count}")