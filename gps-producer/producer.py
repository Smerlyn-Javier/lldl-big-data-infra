import json, os, random, time
from datetime import datetime
from kafka import KafkaProducer
from faker import Faker

faker  = Faker()
topic  = os.getenv("TOPIC", "truck-gps")
broker = os.getenv("BOOTSTRAP_SERVERS", "kafka:9092")

producer = KafkaProducer(
    bootstrap_servers=broker,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TRUCK_IDS = [f"LL-{i:03d}" for i in range(1, 10)]  # 10 trucks

while True:
    msg = {
        "truck_id": random.choice(TRUCK_IDS),
        "timestamp": datetime.utcnow().isoformat(),
        "lat": float(faker.latitude()),
        "lon": float(faker.longitude()),
        "speed": round(random.uniform(20, 90), 1)  # km/h
    }
    producer.send(topic, msg)
    time.sleep(0.5)  # 2 messages per second