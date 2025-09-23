

cities = ["Edmonton", "Paris", "Munich", "Berlin", "Amsterdam", "Prague"]

cities.remove("Edmonton")
new_city = input("Enter a city that interests you: ")
cities.append(new_city)
cities.sort()

print("Our list of interesting cities in alphabetical order is:")
print(cities)

cities_in_Germany = ["Munich", "Berlin"]
for city_of_interest in cities:
    if city_of_interest != "Munich" and city_of_interest != "Berlin":
        print(f"{city_of_interest} is an interesting city that we can visit")
