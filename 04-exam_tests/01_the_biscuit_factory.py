biscuits_per_day_per_worker = int(input())
count_workers = int(input())
number_of_biscuits_competitive = int(input()) # for 30 days

import math
count_days = 1
production_within_30_days = 0

for day in range(1, 30 + 1):
    all_biscuits_per_day = count_workers * biscuits_per_day_per_worker
    if count_days % 3 == 0:
        all_biscuits_third_day = math.floor(count_workers * biscuits_per_day_per_worker * 0.75)
        production_within_30_days += all_biscuits_third_day
        count_days += 1
    else:
        production_within_30_days += all_biscuits_per_day
        count_days += 1
if production_within_30_days > number_of_biscuits_competitive:
    percent = (production_within_30_days - number_of_biscuits_competitive) / number_of_biscuits_competitive * 100
    print(f"You have produced {production_within_30_days} biscuits for the past month.")
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    percent = (number_of_biscuits_competitive - production_within_30_days) / number_of_biscuits_competitive * 100
    print(f"You have produced {production_within_30_days} biscuits for the past month.")
    print(f"You produce {percent:.2f} percent less biscuits.")