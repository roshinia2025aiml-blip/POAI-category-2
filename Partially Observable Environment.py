# Partially Observable Environment

print("===== Search and Rescue Drone =====")

visibility = input("Enter visibility (Clear/Poor): ").capitalize()
temperature = float(input("Enter thermal sensor temperature (°C): "))

if visibility == "Clear":
    print("\nVictim detected.")
    print("Drone moving for rescue.")
else:
    if temperature > 36:
        print("\nPossible human detected using thermal camera.")
        print("Drone moving carefully for rescue.")
    else:
        print("\nNo victim detected.")
        print("Continue scanning the area.")
