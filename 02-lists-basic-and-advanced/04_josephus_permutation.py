people_in_circle = [int(person) for person in input().split()]
term_for_execution = int(input())
executed_people = []
current_index = 0

while True:
    if len(people_in_circle) == 0:
        break
    else:
        index_to_execute = (current_index + term_for_execution-1) % len(people_in_circle)
        executed_person = people_in_circle.pop(index_to_execute)
        executed_people.append(str(executed_person))
        current_index = index_to_execute
print("[" + ",".join(executed_people) + "]")
