docker compose down
docker volume create mongodb
docker volume create caddy
docker compose build
docker compose up