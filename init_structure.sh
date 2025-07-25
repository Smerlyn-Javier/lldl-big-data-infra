# -----------------------------------------------------------------------------
# init_structure.sh  –  Crea el esqueleto del proyecto "lldl-big-data-infra"
# -----------------------------------------------------------------------------

set -e

ROOT="lldl-big-data-infra"

echo "Creando árbol de directorios…"
mkdir -p "$ROOT"/{docs/diagramas,infra/{helm,init-sql},spark-apps,dags,tests/{unit,integration}}

echo "Creando archivos vacíos principales…"
touch "$ROOT"/{.gitignore,.env.example,README.md,docker-compose.yml}
touch "$ROOT"/infra/init-sql/{postgres_init.sql,02_truck_positions.sql}
touch "$ROOT"/spark-apps/{gps_stream.py,requirements.txt}
touch "$ROOT"/dags/streaming_gps.py
touch "$ROOT"/tests/unit/test_gps_producer.py
touch "$ROOT"/tests/integration/test_stream_pipeline.py


