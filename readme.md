## Overview
A simple RESTful full stack web app using a Python + flask backend, Vue +
Vite front-end, MongoDB database, and Caddy web server.  Containerized via
Docker.

## Requirements
- Docker
- Docker compose

If you want faster builds, you can also use npm and pip to install requirements
locally before building containers.

## Installation
Execute `./install.sh` to:
1. Create two external docker volumes using `docker volume create mongodb` and `docker volume create caddy`
2. Run `npm install` in the `client` directory
3. Run `pip3 install -r requirements.txt` in the `server` directory
4. Run `docker compose build` in the root directory

## Configuration
1. Copy .env.example to .env and update with appropriate values, or leave
   unchanged for local testing
2. Create server/resources/resources.json with sample data for any resources you
   want to serve.  This is not a schema and won't be enforced, however it will
   be used to seed the database via the /resetDB endpoint.

## Usage
1. Execute `./run.sh` to start the docker containers
2. Visit `http://localhost:8080` in a browser to view the front-end
3. Curl `http://localhost:8080/api/` via console to interact with the server directly
