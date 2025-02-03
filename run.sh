source webapp-client/shared/.env
MONGODB_VOLUME=mongodb_${ENV}
docker compose --env-file webapp-client/shared/.env down --volumes
docker volume create $MONGODB_VOLUME
docker volume create caddy
while getopts ":b:v" opt; do
  case $opt in
    v)
      docker volume rm $MONGODB_VOLUME caddy
      docker volume create $MONGODB_VOLUME
      docker volume create caddy
      ;;
    b)
      docker compose --env-file webapp-client/shared/.env build
      ;;
  esac
done
docker compose --env-file webapp-client/shared/.env up --abort-on-container-exit