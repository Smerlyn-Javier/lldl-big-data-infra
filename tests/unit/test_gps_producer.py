import json
from gps_producer.producer import payload  

def test_payload_keys():
    sample = payload()
    assert set(sample.keys()) == {"truck_id", "lat", "lon", "event_time"}
