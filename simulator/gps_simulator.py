import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

vehicles = {
    1: {"latitude": 27.3410, "longitude": 88.6138},
    2: {"latitude": 27.3420, "longitude": 88.6148},
}

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("GPS Simulator started")

while True:
    for vehicle_id, position in vehicles.items():

        position["latitude"] += random.uniform(-0.0005, 0.0005)
        position["longitude"] += random.uniform(-0.0005, 0.0005)

        data = {
            "vehicle_id": vehicle_id,
            "latitude": position["latitude"],
            "longitude": position["longitude"],
            "speed": random.uniform(20, 50),
            "timestamp": time.strftime(
                "%Y-%m-%dT%H:%M:%SZ",
                time.gmtime()
            ),
        }

        client.publish(
            f"vehicles/{vehicle_id}/gps",
            json.dumps(data)
        )

        print(data)

    time.sleep(5)