import random

print("===== AI Delivery Drone =====")


destination = input("Enter Delivery Destination: ")

print("\nChecking Weather Conditions...")

weather = random.choice(["Sunny", "Rainy", "Windy", "Storm"])


if weather == "Sunny":
    print("\nDrone Status : Safe to Fly")
    print("Destination  :", destination)
    print("Action       : Package Delivered Successfully")

elif weather == "Windy":
    print("\nDrone Status : Moderate Risk")
    print("Destination  :", destination)
    print("Action       : Reduce Speed and Continue Delivery")

elif weather == "Rainy":
    print("\nDrone Status : High Risk")
    print("Destination  :", destination)
    print("Action       : Delay Delivery Until Rain Stops")

else:
    print("\nDrone Status : Unsafe")
    print("Destination  :", destination)
    print("Action       : Delivery Cancelled Due to Storm")
