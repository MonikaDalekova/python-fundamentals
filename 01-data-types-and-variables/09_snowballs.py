number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0
for every_snowball in range(1, number_of_snowballs + 1):
    weight_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    value_snowball = (weight_snowball // time_needed) ** quality
    if value_snowball > max_value:
        max_value = value_snowball
        max_weight = weight_snowball
        max_time = time_needed
        max_quality = quality
print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")