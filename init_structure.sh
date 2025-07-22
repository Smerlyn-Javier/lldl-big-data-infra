# -----------------------------------------------------------------------------
# init_structure.sh  –  Crea el esqueleto del proyecto "lldl-big-data-infra"
# -----------------------------------------------------------------------------

set -e

ROOT="lldl-big-data-infra"

echo "Creando árbol de directorios…"
mkdir -p "$ROOT"/{docs/diagramas,infra/{helm,init-sql},spark-apps,dags,scripts,superset/dashboards,tests/{unit,integration}}

echo "Creando archivos vacíos principales…"
touch "$ROOT"/{.gitignore,.env.example,README.md,docker-compose.yml}
touch "$ROOT"/docs/{01_Portada.md,02_Contexto.md,03_Objetivos.md,04_Justificacion.md,05_Planificacion.md,06_Presupuesto.md,07_Arquitectura.md,08_Casos_Uso.md}
touch "$ROOT"/infra/init-sql/{superset_init.sql,postgres_init.sql}
touch "$ROOT"/spark-apps/{gps_stream.py,requirements.txt}
touch "$ROOT"/dags/streaming_gps.py
touch "$ROOT"/scripts/gps_producer.py
touch "$ROOT"/superset/docker-entrypoint.sh
touch "$ROOT"/tests/unit/test_gps_producer.py
touch "$ROOT"/tests/integration/test_stream_pipeline.py

echo "Estructura creada con éxito.  Ahora edita los archivos según el contenido proporcionado."
