docker compose --env-file webapp-client/shared/.env down
docker volume create mongodb
docker volume create caddy
docker compose --env-file webapp-client/shared/.env build
docker compose --env-file webapp-client/shared/.env up