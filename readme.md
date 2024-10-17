## Requirements
- Docker
- Docker compose
- Node >=20.0.0

## Installation
1. Create two external docker volumes using `docker volume create mongodb` and `docker volume create caddy`
2. Run `docker compose build` in the root directory
3. Run `npm install` in the `client` directory

## Running
1. Run `npm run dev` in the `client` directory.  The frontend is not dockerized yet to faciliate instant reloading
2. In a separate terminal, run `docker compose up` in the root directory
3. Visit `http://localhost:3000` in a browser
