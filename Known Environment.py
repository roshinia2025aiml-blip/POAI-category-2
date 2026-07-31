roads = {
    "Home": ["School", "Market"],
    "School": ["Hospital"],
    "Market": ["Hospital"],
    "Hospital": ["Office"]
}

location = "Home"

print("=== GPS ROUTE ===")

while location != "Office":

    print("Current:", location)

    next_places = roads[location]

    location = next_places[0]

print("Reached Office")
