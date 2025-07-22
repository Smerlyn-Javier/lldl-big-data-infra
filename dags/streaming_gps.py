from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG(
    dag_id="spark_gps_stream",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@once",
    catchup=False,
    tags=["spark", "gps"],
) as dag:

    spark_submit = DockerOperator(
        task_id="submit_spark_job",
        image="bitnami/spark:3.5.0",
        api_version="auto",
        auto_remove=True,
        command=(
            "spark-submit --packages "
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 "
            "/opt/spark-apps/gps_stream.py"
        ),
        docker_url="unix://var/run/docker.sock",
        network_mode="lldl-big-data-infra_lldl-net",
        mounts=["/opt/spark-apps:/opt/spark-apps"],
    )
