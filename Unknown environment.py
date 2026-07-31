import random

locations = [
    "Rock",
    "Crater",
    "Ice",
    "Minerals",
    "Sand Dunes",
    "Hill"
]

visited = []

print("=== MARS ROVER ===")

while len(visited) != len(locations):

    place = random.choice(locations)

    if place not in visited:
        visited.append(place)
        print("Discovered:", place)

print("\nMission Complete")
print("Visited Locations:")

for place in visited:
    print(place)
