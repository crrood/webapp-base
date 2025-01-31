docker compose --env-file webapp-client/shared/.env down --volumes
docker volume create mongodb
docker volume create caddy
while getopts ":b:v" opt; do
  case $opt in
    v)
      docker volume rm mongodb caddy
      docker volume create mongodb
      docker volume create caddy
      ;;
    b)
      docker compose --env-file webapp-client/shared/.env build
      ;;
  esac
done
docker compose --env-file webapp-client/shared/.env up --abort-on-container-exit