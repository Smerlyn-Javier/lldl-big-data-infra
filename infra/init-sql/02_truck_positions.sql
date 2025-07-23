CREATE TABLE IF NOT EXISTS public.truck_positions (
  truck_id   varchar(10),
  timestamp  timestamptz,
  lat        double precision,
  lon        double precision,
  speed      numeric(5,1)
);

GRANT INSERT, SELECT ON public.truck_positions TO admin;