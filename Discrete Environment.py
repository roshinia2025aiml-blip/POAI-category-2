grid_size = 5

x = 2
y = 2

commands = ["UP", "UP", "LEFT", "DOWN", "RIGHT", "RIGHT"]

print("=== GRID ROBOT ===")

for command in commands:

    if command == "UP" and x > 0:
        x -= 1

    elif command == "DOWN" and x < grid_size - 1:
        x += 1

    elif command == "LEFT" and y > 0:
        y -= 1

    elif command == "RIGHT" and y < grid_size - 1:
        y += 1

    print(command, "-> Position:", (x, y))
