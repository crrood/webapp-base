## Overview
A simple RESTful full stack web app using:
- Python + flask backend
- Vue + Vite front-end
- MongoDB database
- Caddy web server
- Containerized via Docker

This repo is a coordinator for separate client and server repos, which are
meant to be cloned / forked and worked on separately.  Ideally the server stays
exactly as-is and the client contains all project-specific logic.

## Requirements
- Docker
- Docker compose

If you want faster builds, you can also use npm and pip to install requirements
locally via before building the containers.

## Configuration
1. Run `install.sh` to install requirements and copy `webapp-client/shared/.env.example`
2. Update `webapp-client/shared/resources.json` with sample data for any resources 
   you want to serve

## Usage
1. Execute `./run.sh` to start the docker containers, with the optional `-b`
   flag to build them as well
2. Visit `http://localhost:8080/todo` in a browser to view the front-end
3. Curl `http://localhost:8080/api/` via console to interact with the server directly

The server will create endpoints based on the JSON file in
`webapp-client/shared/resources.json`.  For instance, in the example template
you'll have `/entity` and `/anotherEntity`.  

Each supports several methods:
- `GET /entity` -> an array of all entities
- `GET /entity/$id` -> a single entity keyed on `entity._id.$oid`
- `PUT /entity` -> Creates a new entity, or updates an existing one if the body
  data contains `entity._id.$oid`
- `DELETE /entity/$id` -> deletes the specified entity