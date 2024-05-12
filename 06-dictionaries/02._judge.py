# contest_dict = {}
#
# while True:
#     data = input()
#     if data == "no more time":
#         break
#     username, contest, points = data.split(" -> ")
#     points = int(points)
#     if contest not in contest_dict.keys():
#         contest_dict[contest] = {username: points}
#     else:
#         if username not in contest_dict[contest]:
#             contest_dict[contest][username] = points
#         else:
#             contest_dict[contest][username] = max(contest_dict[contest][username], points)
#
#
# for key, value in contest_dict.items():
#     participants = len(contest_dict[key])
#     print(f" {key}: {participants} participants")
#     sorted_contest_dict = dict(sorted(value.items(), key=lambda item: (-item[1], item[0])))
#     counter = 0
#     for nested_key, nested_value in sorted_contest_dict.items():
#         counter += 1
#         print(f" {counter}.	{nested_key} <::> {nested_value}")
#
# print("Individual standings:")
# user_points = {}
# for contest, users in contest_dict.items():
#
#     for user, points in users.items():
#         if user in user_points:
#             user_points[user] += points
#         else:
#             user_points[user] = points
#
# sorted_max_points = dict(sorted(user_points.items(), key=lambda x: (-x[1], x[0])))
#
# number = 1
# for key, value in sorted_max_points.items():
#     print(f"{number}. {key} -> {value}")
#     number += 1

#2
def contests(username, contest, points):
    if contest not in judge_contests.keys():
        judge_contests[contest] = {username: points}
    else:
        if username not in judge_contests[contest]:
            judge_contests[contest][username] = points
        else:
            judge_contests[contest][username] = max(judge_contests[contest][username], points)
    return judge_contests


def individuals():
    for contest, users in judge_contests.items():
        for name, points in users.items():
            if name in individuals_results.keys():
                individuals_results[name] += points
            else:
                individuals_results[name] = points
    return individuals_results


judge_contests = {}
individuals_results = {}

data = input()
while data != "no more time":
    username, contest, points = data.split(" -> ")
    points = int(points)
    judge_contests = contests(username, contest, points)
    data = input()

for contest, value in judge_contests.items():
    print(f"{contest}: {len(value)} participants")
    sorted_judge = dict(sorted(value.items(), key=lambda item: (-item[1], item[0])))

    number = 1
    for name, points in sorted_judge.items():
        print(f"{number}. {name} <::> {points}")
        number += 1


individuals_results = individuals()
sorted_individuals = dict(sorted(individuals_results.items(), key=lambda item: (-item[1], item[0])))

print(f"Individual standings:")
number = 1
for name, points in sorted_individuals.items():
    print(f"{number}. {name} -> {points}")
    number += 1

