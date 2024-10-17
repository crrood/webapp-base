## Requirements
- Docker
- Docker compose
- npm
- pip

## Installation
Run ./install.sh in the root directory.  This will:
1. Create two external docker volumes using `docker volume create mongodb` and `docker volume create caddy`
2. Run `npm install` in the `client` directory
3. Run `pip3 install -r requirements.txt` in the `server` directory
4. Run `docker compose build` in the root directory

## Usage
1. Run `docker compose up` in the root directory
2. Visit `http://localhost:8080` in a browser to view the front-end
3. Ping `http://localhost:8081` via console to interact with the server directly
