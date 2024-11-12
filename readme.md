## Overview
A simple RESTful full stack web app using a Python + flask backend, Vue +
Vite front-end, MongoDB database, and Caddy web server.  Containerized via
Docker.

This repo is a coordinator for separate client and server repos, which are
meant to be cloned / forked and worked on separately.

## Requirements
- Docker
- Docker compose

If you want faster builds, you can also use npm and pip to install requirements
locally via `install.sh` before building the containers.

## Configuration
1. Copy .env.example to .env and update with appropriate values, or leave
   unchanged for local testing
2. Update resources.json with sample data for any resources you want to serve.  
   This mapping will be used to create endpoints, but is not a schema and won't be 
   enforced.

## Usage
1. Execute `./run.sh` to start the docker containers
2. Visit `http://localhost:8080` in a browser to view the front-end
3. Curl `http://localhost:8080/api/` via console to interact with the server directly
