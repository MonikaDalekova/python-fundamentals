# country = input().split(", ")
# capital = input().split(", ")
#
# matches = {country[index]: capital[index] for index in range(len(country))}
# # matches = dict(zip(country, capital))
#
#
# for country, capital in matches.items():
#     print(f"{country} -> {capital}")

#2
def matches(a, b):
    combined_data = {country: capital for country, capital in zip(a, b)}
    for country, capital in combined_data.items():
        print(f"{country} -> {capital}")


countries = input().split(', ')
capitals = input().split(', ')
matches(countries, capitals)