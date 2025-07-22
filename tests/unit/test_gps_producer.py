import json
from scripts.gps_producer import payload  # refactoriza si tu script cambia

def test_payload_keys():
    sample = payload()
    assert set(sample.keys()) == {"truck_id", "lat", "lon", "event_time"}
