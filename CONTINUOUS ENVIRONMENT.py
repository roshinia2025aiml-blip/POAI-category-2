import random
import time

print("=== DRONE NAVIGATION SYSTEM ===")

x = 0.0
y = 0.0
battery = 100

for step in range(10):
    dx = random.uniform(-3, 3)
    dy = random.uniform(-3, 3)

    x += dx
    y += dy
    battery -= random.randint(2, 5)

    print("\nStep:", step + 1)
    print("Drone Position: ({:.2f}, {:.2f})".format(x, y))
    print("Battery:", battery, "%")

    if battery < 20:
        print("Warning: Low Battery!")

    time.sleep(1)

print("\nMission Completed")
