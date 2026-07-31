import random
import time

temperature = 30

print("=== WEATHER MONITOR ===")

for i in range(10):

    temperature += random.randint(-3, 4)

    print("Current Temperature:", temperature, "°C")

    if temperature > 35:
        print("Hot Weather")

    elif temperature < 25:
        print("Cold Weather")

    else:
        print("Normal Weather")

    time.sleep(1)
