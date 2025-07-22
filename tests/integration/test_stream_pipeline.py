import pytest, os, time, psycopg2
from testcontainers.kafka import KafkaContainer
from testcontainers.postgres import PostgresContainer

@pytest.mark.integration
def test_kafka_to_pg():
    with KafkaContainer() as kafka, PostgresContainer() as pg:
        # Lógica para levantar Spark job contra contenedores efímeros
        # y verificar que las filas lleguen.
        time.sleep(1)
        conn = psycopg2.connect(pg.get_connection_url())
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM truck_positions")
            assert cur.fetchone()[0] > 0
