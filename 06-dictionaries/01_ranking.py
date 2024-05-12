# #1
# contests = {}
# while True:
#     data = input()
#     if data == "end of contests":
#         break
#     contest, password = data.split(":")
#     contests[contest] = password
#
# submissions = {}
# while True:
#     info = input()
#     if info == "end of submissions":
#         break
#     contest, password, username, points = info.split("=>")
#     points = int(points)
#
#     if contest in contests.keys() and password in contests.values():
#         if username not in submissions.keys():
#             submissions[username] = {}
#             submissions[username][contest] = points
#         else:
#             if contest not in submissions[username].keys():
#                 submissions[username][contest] = points
#             else:
#                 # old_points = submissions[username][contest]
#                 # points = max(old_points, points)
#                 submissions[username][contest] = max(submissions[username][contest], points)
# sorted_candidates = {} # сортиране на вложен речник, първо сортира вложения речник по стойност и след това първия по буква
# for key, value in submissions.items():
#     submissions[key] = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
#     sorted_candidates = dict(sorted(submissions.items()))
#
# max_points = 0
# max_user = ""
# for key, value in submissions.items():
#     sum_value = sum(submissions[key].values())
#     if sum_value > max_points:
#         max_points = sum_value
#         max_user = key
# print(f"Best candidate is {max_user} with total {max_points} points.")
# print("Ranking:")
#
# for key, value in sorted_candidates.items():
#     print(f"{key}")
#     for contest, points in value.items():
#         print(f"#  {contest} -> {points}")

#2
# contests = {}
#
# command = input()
# while command != "end of contests":
#     contest, password = command.split(':')
#     if contest not in contests:
#         contests[contest] = password
#
#     command = input()
#
# candidates = {}
#
# command = input()
# while command != "end of submissions":
#     command = command.split('=>')
#     contest = command[0]
#     password = command[1]
#     username = command[2]
#     points = int(command[3])
#     if contest in contests and password == contests[contest]:
#         if username not in candidates:
#             candidates[username] = {contest: points}
#         else:
#             if contest in candidates[username]:
#                 candidates[username][contest] = max(candidates[username][contest], points)
#             else:
#                 candidates[username][contest] = points
#
#     command = input()
#
# sorted_candidates = {}
# for key, value in candidates.items():
#     candidates[key] = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
#     sorted_candidates = dict(sorted(candidates.items()))
# print(sorted_candidates)
#
# max_points = 0
# max_user = ""
# for key, value in candidates.items():
#     sum_value = sum(candidates[key].values())
#     if sum_value > max_points:
#         max_points = sum_value
#         max_user = key
#
# print(f"Best candidate is {max_user} with total {max_points} points.")
# print("Ranking:")
# for key, value in sorted_candidates.items():
#     print(f"{key}")
#     for contest, points in value.items():
#         print(f"#  {contest} -> {points}")

#3
def contests_passwords(command):
    contest, password = command.split(":")
    if contest not in contests:
        contests[contest] = password
    return contests


def submission_dict(username, contest, points):
    if username not in submissions.keys():
        submissions[username] = {}
        submissions[username] = {contest: points}
    else:
        if contest in submissions[username]:
            old_points = submissions[username][contest]
            points = max(old_points, points)
            submissions[username][contest] = max(submissions[username][contest], points)
        else:
            submissions[username][contest] = points
    return submissions


def best_candidate_points():
    best_candidate = ""
    max_points = 0
    for user, info in submissions.items():
        sum_points = sum(info.values())
        if max_points < sum_points:
            max_points = sum_points
            best_candidate = user
    print(f"Best candidate is {best_candidate} with total {max_points} points.")


def sorting_candidates():
    for key, value in submissions.items():
        submissions[key] = dict(sorted(value.items(), key=lambda x: x[1], reverse=True))
        sorted_submission = dict(sorted(submissions.items()))
        return sorted_submission


contests = {}
command = input()
while command != "end of contests":
    contests = contests_passwords(command)
    command = input()

data = input()
submissions = {}
while data != "end of submissions":
    contest, password, username, points = data.split("=>")
    points = int(points)
    if contest in contests.keys() and password in contests.values():
        submissions = submission_dict(username, contest, points)
    data = input()

best_candidate_points()
sorted_submission = sorting_candidates()
for key, value in sorted_submission.items():
    print(f"{key}")
    for contest, points in value.items():
        print(f"#  {contest} -> {points}")