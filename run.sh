#!/bin/bash
while getopts "bcp" opt; do
  case $opt in
    c)
      RESET_CADDY=true
      ;;
    b)
      BUILD=true
      ;;
    p)
      PROD=true
      ;;
  esac
done
if [ $PROD ]; then
  ENV_FILE=webapp-client/shared/.env.prod
else
  ENV_FILE=webapp-client/shared/.env.dev
fi
source ${ENV_FILE}
MONGODB_VOLUME=mongodb_${COMPOSE_PROJECT_NAME}
CADDY_VOLUME=caddy_${COMPOSE_PROJECT_NAME}
docker volume create $MONGODB_VOLUME
docker volume create $CADDY_VOLUME
if [ $RESET_CADDY ]; then
  docker compose --env-file ${ENV_FILE} down --volumes
  docker volume rm $CADDY_VOLUME
  docker volume create $CADDY_VOLUME
fi
if [ $BUILD ]; then
  docker compose --env-file ${ENV_FILE} build
  if [ $PROD ]; then
    cd webapp-client
    if [ "$(npm list | grep vite)" ]; then
      rm -rf ./dist
      cp ./shared/.env.prod .env
      npx vite build
      rm .env
      cd ..
    else
      echo "vite not installed in webapp-client, run 'npm install'"
      cd ..
      exit 1
    fi
  fi
fi
docker compose --env-file ${ENV_FILE} up --abort-on-container-exit
docker compose --env-file ${ENV_FILE} down --volumes