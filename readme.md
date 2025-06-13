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
1. Execute `./run.sh -b` to build and start the docker containers
2. On the first run, go to `http://localhost:8080/api/resetDB` in a browser or
   via curl to load the data from `resources.json`
3. Visit `http://localhost:8080/resourceA` in a browser to view the front-end
4. Curl `http://localhost:8080/api/` via console to interact with the server directly

The server will create endpoints based on the JSON file in
`webapp-client/shared/resources.json`.  For instance, in the example template
you'll have `/resourceA` and `/resourceB`.  

Each supports several server-side methods:
- `GET /api/<resource>` -> an array of all resources
- `GET /api/<resource>/$id` -> a single resource keyed on `resource._id.$oid`
- `PUT /api/<resource>` -> Creates a new resource, or updates an existing one if the body
  data contains `<resource>._id.$oid`
- `DELETE /api/<resource>/$id` -> deletes the specified resource

There is also a utility method `/api/resetDB` which will reset the DB state to match
`resources.json`, and `/api/testDB` which will run a suite of tests to make sure
everything's working.

The front-end comes with a basic page to list all the instances of ResourceA and show the
details of a single one.