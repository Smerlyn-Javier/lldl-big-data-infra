-- Crea rol dedicado para Superset y otorga permisos mínimos
CREATE ROLE superset LOGIN PASSWORD 'superset';
GRANT CONNECT ON DATABASE ${POSTGRES_DB} TO superset;
GRANT USAGE ON SCHEMA public TO superset;
