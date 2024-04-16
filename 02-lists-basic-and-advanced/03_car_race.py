time_per_step = [int(time) for time in input().split()]
middle_point = len(time_per_step) // 2
left_car_time = time_per_step[:middle_point]
right_car_time = time_per_step[middle_point+1:]
sum_left = 0
sum_right = 0
for number in left_car_time:
    sum_left += number
    if number == 0:
        sum_left -= 0.2 * sum_left
right_car_time.reverse()
for number in right_car_time:
    sum_right += number
    if number == 0:
        sum_right -= 0.2*sum_right
if sum_left > sum_right:
    print(f"The winner is right with total time: {sum_right:.1f}")
elif sum_left < sum_right:
    print(f"The winner is left with total time: {sum_left:.1f}")

