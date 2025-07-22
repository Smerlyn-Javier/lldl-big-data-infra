#!/usr/bin/env python
"""
Envia posiciones GPS sintéticas a Kafka cada segundo.
"""
import json, time, uuid, random
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")

TRUCK_IDS = [f"TRK{str(i).zfill(3)}" for i in range(1, 11)]

while True:
    payload = {
        "truck_id": random.choice(TRUCK_IDS),
        "lat": round(random.uniform(18.4, 19.1), 6),
        "lon": round(random.uniform(-70.2, -69.3), 6),
        "event_time": datetime.utcnow().isoformat()
    }
    producer.send("gps", json.dumps(payload).encode())
    print("Enviado:", payload)
    time.sleep(1)
