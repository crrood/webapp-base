docker compose --env-file webapp-client/shared/.env down
while getopts "b" opt; do
  case $opt in
    b)
      docker volume create mongodb
      docker volume create caddy
      docker compose --env-file webapp-client/shared/.env build
      ;;
  esac
done
docker compose --env-file webapp-client/shared/.env up