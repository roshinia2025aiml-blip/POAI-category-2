package_location = input("Enter package location (A1/B2/C3): ").upper()

if package_location == "A1":
    print("Move to Shelf A1 and pick the package.")
elif package_location == "B2":
    print("Move to Shelf B2 and pick the package.")
else:
    print("Package not found.")
