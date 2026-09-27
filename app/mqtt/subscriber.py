import json
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

from app.db.database import SessionLocal
from app.models import GPSRecord

import os

MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_TOPIC = "vehicles/+/gps"


def on_connect(client, userdata, flags, rc):
    print("MQTT connected")
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())

        vehicle_id = int(data["vehicle_id"])

        timestamp = data.get("timestamp")

        if timestamp:
            timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        else:
            timestamp = datetime.now(timezone.utc)

        db = SessionLocal()

        record = GPSRecord(
            vehicle_id=vehicle_id,
            latitude=float(data["latitude"]),
            longitude=float(data["longitude"]),
            speed=float(data["speed"]),
            timestamp=timestamp,
        )

        db.add(record)
        db.commit()
        db.close()

        print("GPS saved:", data)

    except Exception as e:
        print("MQTT error:", e)


def start_mqtt():
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    client.loop_start()

    return client