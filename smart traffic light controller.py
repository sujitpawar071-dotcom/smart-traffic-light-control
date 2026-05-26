# Smart Traffic Light Controller using Python

import time
import random

# Traffic signals
signals = ["North", "South", "East", "West"]

# Function to generate random vehicle count
def get_vehicle_count():
    return random.randint(0, 50)

# Main traffic control loop
while True:

    traffic_data = {}

    print("\n===== Vehicle Density =====")

    # Get vehicle count for each direction
    for signal in signals:
        traffic_data[signal] = get_vehicle_count()
        print(signal, ":", traffic_data[signal], "vehicles")

    # Find direction with highest traffic
    green_signal = max(traffic_data, key=traffic_data.get)

    print("\nGreen Signal:", green_signal)

    # Green light timing based on traffic density
    green_time = traffic_data[green_signal] // 5

    if green_time < 5:
        green_time = 5

    print("Green Light Duration:", green_time, "seconds")

    # Simulate traffic signal
    for i in range(green_time, 0, -1):
        print("Remaining Time:", i, "seconds")
        time.sleep(1)

    print("\nSignal Switching...\n")

    # Repeat continuously
