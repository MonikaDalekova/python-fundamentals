taxed_vehicles = input().split(">>")

initial_family = 50
initial_heavyDuty = 80
initial_sports = 100

total_tax_collected = 0

for vehicle in taxed_vehicles:
    car_type, years_to_pay, traveled_kilometers = vehicle.split()
    years_to_pay = int(years_to_pay)
    traveled_kilometers = int(traveled_kilometers)
    total_tax_to_pay = 0
    if car_type == "family" or car_type == "heavyDuty" or car_type == "sports":

        if car_type == "family":
            total_tax_to_pay += initial_family
            for every_year in range(1, years_to_pay + 1):
                total_tax_to_pay -= 5
            total_tax_to_pay += (traveled_kilometers // 3000) * 12
            total_tax_collected += total_tax_to_pay

        elif car_type == "heavyDuty":
            total_tax_to_pay += initial_heavyDuty
            for every_year in range(1, years_to_pay + 1):
                total_tax_to_pay -= 8
            total_tax_to_pay += (traveled_kilometers // 9000) * 14
            total_tax_collected += total_tax_to_pay

        elif car_type == "sports":
            total_tax_to_pay += initial_sports
            for every_year in range(1, years_to_pay + 1):
                total_tax_to_pay -= 9
            total_tax_to_pay += (traveled_kilometers // 2000) * 18
            total_tax_collected += total_tax_to_pay
        print(f"A {car_type} car will pay {total_tax_to_pay:.2f} euros in taxes.")
    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")