# Deterministic Environment

print("===== Smart Elevator =====")

current = int(input("Enter Current Floor: "))
destination = int(input("Enter Destination Floor: "))

distance = abs(destination-current)

print("\nElevator Status")
print("--------------------")
print("Current Floor :", current)
print("Destination   :", destination)
print("Floors Travel :", distance)

if destination > current:
    print("Direction : UP")
elif destination < current:
    print("Direction : DOWN")
else:
    print("Already at Destination")
