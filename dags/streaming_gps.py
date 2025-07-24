from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount
from airflow.models.baseoperator import chain
from airflow.operators.empty import EmptyOperator
from datetime import timedelta

PROJECT_DIR = "/Users/imac/lldl-big-data-infra"


default_args = {"retries": 2, "retry_delay": timedelta(minutes=5)}

with DAG(
    dag_id="spark_gps_stream",
    start_date=days_ago(1),
    schedule_interval="@once",
    catchup=False,
    tags=["spark", "gps"],
    default_args=default_args,
) as dag:

    start = EmptyOperator(task_id="start")

    spark_submit = DockerOperator(
        task_id="submit_spark_job",
        image="bitnami/spark:3.5.0",
        api_version="auto",
        auto_remove=False,           
        tty=True,
        command=(
            "bash -c 'set -eo pipefail; "
            "export SPARK_PRINT_LAUNCH_COMMAND=1; "
            "LOG_DIR=/opt/spark-apps/logs; mkdir -p ${LOG_DIR}; "
            "spark-submit "
            "--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,"
            "org.postgresql:postgresql:42.7.3 "
            "--master spark://spark-master:7077 "
            "--deploy-mode client "
            "/opt/spark-apps/gps_stream.py "
            "2>&1 | tee ${LOG_DIR}/gps_stream_$(date +%s).log'"
        ),
        mounts=[
            Mount(
                "${PROJECT_DIR}/spark-apps",
                "/opt/spark-apps",
                "bind",
                read_only=True,
            ),
            Mount("spark-checkpoints", "/opt/spark-checkpoints", "volume"),
        ],
        network_mode="lldl-net",
        docker_url="unix://var/run/docker.sock",
    )

    end = EmptyOperator(task_id="end")

    chain(start, spark_submit, end)
